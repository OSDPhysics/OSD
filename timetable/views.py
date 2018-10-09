from django.shortcuts import render, redirect, reverse
from .models import *
from school.models import Teacher
from django.contrib.auth.decorators import login_required
from osd.settings.base import CALENDAR_START_DATE
from timetable.forms import LessonCopyForm
from osd.decorators import *
import datetime
from django.http import HttpResponseForbidden


# Create your views here.

def get_monday_date_from_weekno(week_number):
    start_date = CALENDAR_START_DATE + datetime.timedelta(weeks=week_number)
    return start_date


def generate_week_grid(teacher, week_number):
    start_date = get_monday_date_from_weekno(week_number)
    next_week = week_number + 1
    if week_number is not 0:
        last_week = week_number - 1
    else:
        last_week = 0

    current_date = start_date
    weekgrid = []
    for day in DAYS:

        # Check if the day is suspended.
        suspensions = LessonSuspension.objects.filter(date=current_date)
        if suspensions.exists():
            # There is at least one suspension on this day
            if suspensions.filter(whole_school=True).exists():
                if suspensions.filter(all_day=True).exists():
                    # Get the first suspension TODO: add constraints so there's only one
                    suspension = suspensions.filter(all_day=True)[0]

                    # fill the day row with the suspension objects
                    weekgrid.append([day[0], suspension, suspension, suspension, suspension])
                    current_date = current_date + datetime.timedelta(days=1)
                    continue



        dayrow = [day[0]]

        for period in PERIODS: # The day isn't suspended, but what about the period?
            # Check if that period is whole-school suspended:
            check = suspensions.filter(period=period[0]).filter(whole_school=True)
            if check.exists():
                dayrow.append(check[0])  # Add that the day is suspended

                continue

            try:
                timetabled_lesson = TimetabledLesson.objects.get(lesson_slot__day=day[0],
                                                                 classgroup__groupteacher=teacher,
                                                                 lesson_slot__period=period[0])
            except TimetabledLesson.DoesNotExist:
                dayrow.append("Free")
                timetabled_lesson = "Free"

            if timetabled_lesson != "Free":
                check = suspensions.filter(period=period[0], classgroups=timetabled_lesson.classgroup)
                if check.exists():
                    dayrow.append(check)
                    continue

                check = suspensions.filter(classgroups=timetabled_lesson.classgroup, all_day=True).exists()

                if check:
                    dayrow.append(check)
                    continue

                else:
                    try:
                        lesson = Lesson.objects.get(lessonslot=timetabled_lesson, date=current_date)
                        dayrow.append(lesson)
                    except models.ObjectDoesNotExist:
                        from timetable.models import set_classgroups_lesson_dates
                        set_classgroups_lesson_dates(timetabled_lesson.classgroup)
                        lesson = Lesson.objects.get(lessonslot=timetabled_lesson, date=current_date)
                        dayrow.append(lesson)

        weekgrid.append(dayrow)
        current_date = current_date + datetime.timedelta(days=1)

    return weekgrid


def check_suspension(date, period, classgroup):
    # Check if the whole school is suspended that day:
    day_suspensions = LessonSuspension.objects.filter(date=date)
    suspensions = day_suspensions.filter(whole_school=True, all_day=True).count()
    if suspensions:
        return True

    suspensions = day_suspensions.filter(period=period, whole_school=True).count()
    if suspensions:
        return True

    suspensions = day_suspensions.filter(all_day=True, classgroups=classgroup).count()
    if suspensions:
        return True

    suspensions = day_suspensions.filter(period=period, classgroups=classgroup).count()
    if suspensions:
        return True

    return False


@login_required
def teacher_splash(request):
    teacher = Teacher.objects.get(user=request.user)
    week_number = datetime.datetime.now().isocalendar()[1] - CALENDAR_START_DATE.isocalendar()[1]
    if week_number < 0:
        week_number = 0

    return redirect(reverse('timetable:teacher_tt', args=[teacher.pk, week_number]))

    # Create a grid to show the days in


def teacher_tt(request, teacher_pk, week_number):
    teacher = Teacher.objects.get(pk=teacher_pk)
    start_date = get_monday_date_from_weekno(week_number)
    next_week = week_number + 1
    if week_number is not 0:
        last_week = week_number - 1
    else:
        last_week = 0

    weekgrid = generate_week_grid(teacher, week_number)

    return render(request, 'timetable/splash.html', {'weekgrid': weekgrid,
                                                     'start_day': start_date,
                                                     'next_week': next_week,
                                                     'last_week': last_week,
                                                     'teacher': teacher})


@teacher_only
def class_lesson_list(request, classgroup_pk):
    classgroup = ClassGroup.objects.get(pk=classgroup_pk)
    lessons = Lesson.objects.filter(lessonslot__classgroup=classgroup_pk).order_by("sequence")

    # Check for any lessons beyond end date
    overshot_lessons = Lesson.objects.filter(date__gt=CALENDAR_END_DATE, classgroup=classgroup).count()
    if overshot_lessons:
        messages.add_message(request, messages.WARNING, 'Lessons exist past end of school year.')

    return render(request, 'timetable/classgroup_lesson_list.html', {'classgroup': classgroup,
                                                                     'lessons': lessons})


@teacher_only
def copy_lesson(request, lesson_pk):
    source_lesson = Lesson.objects.get(pk=lesson_pk)
    moveForm = LessonCopyForm()

    if request.method == 'POST':
        moveForm = LessonCopyForm(request.POST)
        if moveForm.is_valid():

            target_lesson = moveForm.cleaned_data['lesson_to_copy_to']
            if target_lesson.lesson_title:
                # The lesson has already been written, so we need to move it first
                return
            else:
                target_lesson.lesson_title = source_lesson.lesson_title
                target_lesson.requirements = source_lesson.requirements
                target_lesson.description = source_lesson.description

                for point in source_lesson.syllabus_points_covered.all():
                    target_lesson.syllabus_points_covered.add(point)

                target_lesson.save()
                # Now copy the resources
                for resource in source_lesson.resources().all():
                    new_resource = LessonResources.objects.create(lesson=target_lesson,
                                                                  resource_type=resource.resource_type,
                                                                  resource_name=resource.resource_name,
                                                                  link=resource.link,
                                                                  students_can_view_after=resource.students_can_view_after,
                                                                  students_can_view_before=resource.students_can_view_before)
                    new_resource.save()

            return redirect(reverse('timetable:class_lesson_list', args=[source_lesson.classgroup.pk, ]))

        else:
            return render(request, 'timetable/move_lesson.html', {'moveform': moveForm})

    else:
        return render(request, 'timetable/move_lesson.html', {'moveform': moveForm})


@teacher_only
def delete_lesson(request, lesson_pk, class_pk):
    lesson = Lesson.objects.get(pk=lesson_pk)
    classgroup = ClassGroup.objects.get(pk=class_pk)
    if not lesson.lesson_title:
        lesson.delete()
        messages.add_message(request, messages.SUCCESS, 'Lesson deleted successfully.')
        return redirect(reverse('timetable:class_lesson_list', args=[class_pk, ]))

    else:
        return render(request, 'timetable/confirm_delete.html', {'lesson': lesson,
                                                                 'classgroup': classgroup})


@teacher_only
def confirm_delete_lesson(request, lesson_pk, class_pk):
    lesson = Lesson.objects.get(pk=lesson_pk)
    lesson.delete()
    messages.add_message(request, messages.SUCCESS, 'Lesson deleted successfully.')
    return redirect(reverse('timetable:class_lesson_list', args=[class_pk, ]))


def get_lesson_from_date(classgroup, date):
    # get the lessons

    lesson_slots = TimetabledLesson.objects.filter(classgroup=classgroup)

    # find the sequence number from the date

    lessons_per_week = lesson_slots[0].total_lessons()


@teacher_only
def class_lesson_check(request, classgroup_pk):
    classgroup = ClassGroup.objects.get(pk=classgroup_pk)
    # re-order all the lessons

    message = set_classgroups_lesson_dates(classgroup)

    if message:
        messages.add_message(request, messages.WARNING, message)

    return redirect(reverse('timetable:class_lesson_list', args=[classgroup_pk, ]))


@login_required
def lesson_details(request, lesson_pk):
    lesson = Lesson.objects.get(pk=lesson_pk)

    # TEACHERS should see all details
    if request.user.groups.filter(name='Teachers').exists():
        return render(request, 'timetable/teacher_lesson_details.html', {'lesson': lesson})

    # STUDENTS see restricted data
    elif request.user.groups.filter(name='Students').exists():
        classgroups = Student.objects.get(user=request.user).classgroups.all()

        # Make sure student can see this classgroup
        if lesson.classgroup in classgroups:
            resources = lesson.student_viewable_resources()
            return render(request, 'timetable/student_lesson_details.html', {'lesson': lesson,
                                                                             'resources': resources})

        else:  # Student is not a member of this lessons classgroup
            return HttpResponseForbidden()

    else:  # Not a student or a teacher!
        return HttpResponseForbidden()
