from django.shortcuts import render, redirect, reverse
from .models import *
from school.models import Teacher
from django.contrib.auth.decorators import login_required
from osd.settings.base import CALENDAR_START_DATE
import datetime

# Create your views here.

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

    current_date = start_date
    weekgrid = []
    for day in DAYS:
        currentday = [day[0]]
        for period in PERIODS:
            day = currentday[0] # TODO: clean up this ugly hack
            period = int(period[0])
            lessonslot = LessonSlot.objects.get(day=day, period=period)
            timetabledlesson = []
            try:
                lessonslot = TimetabledLesson.objects.get(classgroup__groupteacher=teacher, lesson_slot=lessonslot)
                string = str("<a href='/timetable/class/" + str(lessonslot.classgroup.pk)+ "'>" + str(lessonslot.classgroup) + "</a>")
                timetabledlesson.append(string)
            except TimetabledLesson.DoesNotExist:
                timetabledlesson.append("FREE")

            if timetabledlesson[0] is not 'FREE':

                lesson, created = Lesson.objects.get_or_create(date=current_date, lesson=lessonslot)
                edit_string = str("<a href=/admin/timetable/lesson/" + str(lesson.pk) + "/change target='_blank'>" + str(lesson.title) + "</a>")
                timetabledlesson.append(edit_string)
                if lesson.description:
                    timetabledlesson.append(lesson.description)

                if lesson.requirements:
                    timetabledlesson.append("<b>Order:</b> " + lesson.requirements)


            currentday.append(timetabledlesson)
        weekgrid.append(currentday)
        current_date = current_date + datetime.timedelta(days=1)

    return render(request, 'timetable/splash.html', {'weekgrid': weekgrid,
                                                     'start_day': start_date,
                                                     'next_week': next_week,
                                                     'last_week': last_week,
                                                     'teacher_pk': teacher_pk})




def get_monday_date_from_weekno(week_number):
    start_date = CALENDAR_START_DATE + datetime.timedelta(weeks=week_number)
    return start_date


def class_lesson_list(request, classgroup_pk):
    classgroup = ClassGroup.objects.get(pk=classgroup_pk)
    lessons = Lesson.objects.filter(lesson__classgroup=classgroup_pk)
    lessons.order_by("date")

    return render(request, 'timetable/classgroup_lesson_list.html', {'classgroup': classgroup,
                                                                     'lessons': lessons})