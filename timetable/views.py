from django.shortcuts import render, redirect, reverse
from .models import *
from school.models import Teacher
from django.contrib.auth.decorators import login_required
from osd.settings.base import CALENDAR_START_DATE
from timetable.forms import LessonCopyForm, LessonForm, AddLessonSuspensions, LessonResourceForm, LessonSearchForm
from tracker.forms import MPTTSyllabusForm
from osd.decorators import *
import datetime
from django.http import HttpResponseForbidden
from django.contrib import messages
from .functions import get_monday_date_from_weekno, get_weekno_from_date, get_next_tt_week_year, \
    get_previous_tt_week_year


# Create your views here.

def generate_week_grid(teacher, week_number, year):
    start_date = get_monday_date_from_weekno(week_number, year)

    current_date = start_date
    weekgrid = []
    for day in DAYS:

        # Build the HMTL text to display day and date:
        day_name = day[0]
        day_text = str(day_name) + "<br>" + str(current_date.strftime("%d %b %y"))

        # Check if the day is suspended:
        suspensions = LessonSuspension.objects.filter(date=current_date)

        if suspensions.exists():
            first_suspension = suspensions[0]
            # There is at least one suspension on this day
            if suspensions.filter(whole_school=True).exists():
                if suspensions.filter(all_day=True).exists():
                    # Get the first suspension TODO: add constraints so there's only one
                    suspension = suspensions.filter(all_day=True)[0]

                    # fill the day row with the suspension objects
                    weekgrid.append([day[0], suspension, suspension, suspension, suspension])
                    current_date = current_date + datetime.timedelta(days=1)
                    continue  # Starts the next day in the loop

        dayrow = [day_text]

        for period in PERIODS:  # The day isn't suspended, but what about the period?
            # Check if that period is whole-school suspended:
            check = suspensions.filter(period=period[0]).filter(whole_school=True)
            if check.exists():
                dayrow.append(check[0])  # Add that the lesson is suspended

                continue

            try:
                timetabled_lesson = TimetabledLesson.objects \
                    .get(lesson_slot__day=day[0],
                         classgroup__groupteacher=teacher,
                         lesson_slot__period=period[0],
                         lesson_slot__year=year)
            except TimetabledLesson.DoesNotExist:
                dayrow.append("Free")
                timetabled_lesson = "Free"

            if timetabled_lesson != "Free":
                # We might have suspended just this classgroup
                check = suspensions.filter(period=period[0], classgroups=timetabled_lesson.classgroup)
                if check.exists():
                    dayrow.append(check)
                    continue

                # Now check if the class is suspended all day:
                check = suspensions.filter(all_day=True, classgroups=timetabled_lesson.classgroup)
                if check.exists():
                    dayrow.append(check[0])
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
    today = datetime.date.today()
    from .models import get_year_from_date
    year = get_year_from_date(today)
    week_number = get_weekno_from_date(today, year)

    return redirect(reverse('timetable:teacher_tt', args=[teacher.pk, week_number, year]))


@teacher_only
def teacher_tt(request, teacher_pk, week_number, year):
    teacher = Teacher.objects.get(pk=teacher_pk)
    start_date = get_monday_date_from_weekno(week_number, year)
    next_week, next_year = get_next_tt_week_year(week_number, year)

    last_week, last_year = get_previous_tt_week_year(week_number, year)
    weekgrid = generate_week_grid(teacher, week_number, year)

    return render(request,
                  'timetable/splash2.html',
                  {'weekgrid': weekgrid,
                   'start_day': start_date,
                   'next_week': next_week,
                   'next_year': next_year,
                   'last_week': last_week,
                   'last_year': last_year,
                   'teacher': teacher,
                   'year': year})

@teacher_only
def next_week(request):
    teacher = Teacher.objects.get(user=request.user)
    today = datetime.date.today()
    from .models import get_year_from_date
    year = get_year_from_date(today)
    week_number = get_weekno_from_date(today, year) + 1

    return redirect(reverse('timetable:teacher_tt', args=[teacher.pk, week_number, year]))



@teacher_or_own_classgroup
def class_lesson_list(request, classgroup_pk):
    classgroup = ClassGroup.objects.get(pk=classgroup_pk)
    lessons = Lesson.objects.filter(lessonslot__classgroup=classgroup_pk).order_by("sequence")

    # Check for any lessons beyond end date
    overshot_lessons = Lesson.objects.filter(date__gt=CALENDAR_END_DATE[classgroup.year_taught], classgroup=classgroup).count()
    if overshot_lessons:
        messages.add_message(request, messages.WARNING, 'Lessons exist past end of school year.')

    # Return an unrestricted view for Teachers

    if request.user.groups.filter(name='Teachers'):
        return render(request, 'timetable/classgroup_lesson_list.html', {'classgroup': classgroup,
                                                                         'lessons': lessons})

    # And a restricted one for students etc:

    else:
        return render(request, 'timetable/classgroup_lesson_list_student.html', {'classgroup': classgroup,
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
        return class_lesson_check(request, lesson.classgroup.pk)


    else:
        return render(request, 'timetable/confirm_delete.html', {'lesson': lesson,
                                                                 'classgroup': classgroup})


@teacher_only
def confirm_delete_lesson(request, lesson_pk, class_pk):
    lesson = Lesson.objects.get(pk=lesson_pk)
    lesson.delete()
    messages.add_message(request, messages.SUCCESS, 'Lesson deleted successfully.')
    return class_lesson_check(request, class_pk)


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


@teacher_only
def insert_lesson(request, lesson_pk):
    prev_lesson = Lesson.objects.get(pk=lesson_pk)
    following_lessons = Lesson.objects.filter(sequence__gt=prev_lesson.sequence,
                                              classgroup=prev_lesson.classgroup).order_by('sequence').reverse()
    for lesson in following_lessons:
        lesson.sequence = lesson.sequence + 1
        lesson.save()

    new_lesson = Lesson.objects.create(classgroup=prev_lesson.classgroup,
                                       sequence=prev_lesson.sequence + 1,
                                       lessonslot=prev_lesson.lessonslot
                                       # this is only temporary as we're about to check this.
                                       )

    messages.add_message(request, messages.SUCCESS, 'Lesson added successfully')

    return class_lesson_check(request, prev_lesson.classgroup.pk)


@teacher_only
def move_lesson_up(request, lesson_pk):
    target_lesson = Lesson.objects.get(pk=lesson_pk)
    prev_lesson = Lesson.objects.get(classgroup=target_lesson.classgroup,
                                     sequence=target_lesson.sequence - 1)

    # We need to temporarily re-sequence the previous lesson so it doesn't cause a UNIQUE error
    max_sequence = Lesson.objects.filter(classgroup=target_lesson.classgroup).aggregate(Max("sequence"))
    max = max_sequence['sequence__max'] + 1
    target_lesson.sequence = prev_lesson.sequence
    prev_lesson.sequence = max
    prev_lesson.save()
    target_lesson.save()
    prev_lesson.sequence = target_lesson.sequence + 1
    prev_lesson.save()

    return class_lesson_check(request, prev_lesson.classgroup.pk)


@teacher_only
def move_lesson_down(request, lesson_pk):
    target_lesson = Lesson.objects.get(pk=lesson_pk)
    next_lesson = Lesson.objects.get(classgroup=target_lesson.classgroup,
                                     sequence=target_lesson.sequence + 1)

    # We need to temporarily re-sequence the previous lesson so it doesn't cause a UNIQUE error
    max_sequence = Lesson.objects.filter(classgroup=target_lesson.classgroup).aggregate(Max("sequence"))
    max = max_sequence['sequence__max'] + 1
    target_lesson.sequence = next_lesson.sequence
    next_lesson.sequence = max
    next_lesson.save()
    target_lesson.save()
    next_lesson.sequence = target_lesson.sequence - 1
    next_lesson.save()

    return class_lesson_check(request, next_lesson.classgroup.pk)


@teacher_only
def edit_lesson(request, lesson_pk):
    lesson = Lesson.objects.get(pk=lesson_pk)
    lesson_form = LessonForm(instance=lesson)
    parent_form = MPTTSyllabusForm()
    lesson_search_form = LessonSearchForm()
    if request.method == 'POST':
        lesson_form = LessonForm(request.POST, instance=lesson)
        if lesson_form.is_valid():
            lesson_form.save()
            messages.add_message(request, messages.SUCCESS, 'Lesson saved')

            # check homework is set for a lesson date:
            if lesson_form.cleaned_data['homework_due']:
                if not Lesson.objects.filter(date=lesson_form.cleaned_data['homework_due'],
                                             classgroup=lesson.classgroup).count():
                    messages.add_message(request, messages.WARNING,
                                         "Homework set for a date on which you don't teach this class.")

            # redirect depending on whether we're adding a resource or saving:
            if 'add_resource' in request.POST:
                resource = LessonResources.objects.create(lesson=lesson)
                return redirect(reverse('timetable:edit_lesson_resource', args=[lesson_pk, resource.pk]))

            if 'next_lesson' in request.POST:
                return redirect(reverse('timetable:edit_lesson', args=[lesson.next_in_order().pk]))

            if 'classgroup_lessons' in request.POST:
                return redirect(reverse('timetable:class_lesson_list', args=[lesson.classgroup.pk]))

            if 'rtn_tt' in request.POST:
                return redirect(reverse('timetable:teacher_splash'))


        else:
            messages.add_message(request, messages.ERROR, 'Please correct the errors below')
    return render(request, 'timetable/edit_lesson.html', {'lesson_form': lesson_form,
                                                          'lesson': lesson,
                                                          'parent_form': parent_form,
                                                          'lesson_search_form': lesson_search_form})


@teacher_only
def edit_lesson_resource(request, lesson_pk, resource_pk):
    resource = LessonResources.objects.get(pk=resource_pk)
    lesson_resource_form = LessonResourceForm(instance=resource)
    lesson = Lesson.objects.get(pk=lesson_pk)

    if request.method == 'POST':
        lesson_resource_form = LessonResourceForm(request.POST, instance=resource)
        if lesson_resource_form.is_valid():
            lesson_resource_form.save()
            messages.add_message(request, messages.SUCCESS, 'Resource saved')
            return redirect(reverse('timetable:edit_lesson', args=[lesson_pk, ]))

    return render(request, 'timetable/edit_resource.html', {'resource': resource,
                                                            'lesson': lesson,
                                                            'lesson_resource_form': lesson_resource_form})


@admin_only
def create_multiple_lesson_suspensions(request):
    suspension_form = AddLessonSuspensions

    if request.method == 'POST':
        suspension_form = AddLessonSuspensions(request.POST)
        if suspension_form.is_valid():
            reason = suspension_form.cleaned_data['reason']
            start_date = suspension_form.cleaned_data['start_date']
            end_date = suspension_form.cleaned_data['end_date']
            whole_school = suspension_form.cleaned_data['whole_school']
            current_date = start_date

            while current_date <= end_date:
                suspension = LessonSuspension.objects.create(date=current_date,
                                                             whole_school=whole_school,
                                                             all_day=True,
                                                             reason=reason,
                                                             )

                if not whole_school:
                    for classgroup in suspension_form.cleaned_data['classgroups']:
                        suspension.classgroups.add(classgroup)

                current_date = current_date + datetime.timedelta(days=1)
        return redirect(reverse('timetable:teacher_splash'))

    return render(request, 'timetable/create_multiple_day_suspensions.html', {'suspension_form': suspension_form})


def new_teacher_tt(request, teacher_pk, week_number, year):
    teacher = Teacher.objects.get(pk=teacher_pk)
    start_date = get_monday_date_from_weekno(week_number, year)
    next_week, next_year = get_next_tt_week_year(week_number, year)

    last_week, last_year = get_previous_tt_week_year(week_number, year)

    teachers_classgroups = ClassGroup.objects.filter(groupteacher=teacher)


    lessons = Lesson.objects.filter(date__gte=start_date,
                                            date__lt=next_week,
                                            lessonslot__classgroup__groupteacher=teacher).order_by('date', 'lessonslot.period')

    suspensions = LessonSuspension.objects.filter(date__gte=start_date,
                                                  date__lt=next_week)

# def new_weekgrid(lessons=Lesson.objects.none(), suspensions=LessonSuspension.objects.none(), teacher_classgroups=ClassGroup.objects.none())
#
#     days = []
#     for day in DAYS:
#         day_dictionary = {'day': day}
#         periods = []
#         for period in PERIODS:
#             lesson = lessons.filter(lessonslot=period)
#             if lesson.count():

