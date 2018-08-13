from django.shortcuts import render
from .models import *
from school.models import Teacher

# Create your views here.


def teacher_splash(request):
    teacher = Teacher.objects.get(user=request.user)

    # Create a grid to show the days in

    weekgrid = []
    for day in DAYS:
        currentday = [day[0]]
        for period in PERIODS:
            day = currentday[0] # TODO: clean up this ugly hack
            period = int(period[0])
            lessonslot = LessonSlot.objects.get(day=day, period=period)
            try:
                timetabledlesson = TimetabledLesson.objects.get(classgroup__groupteacher=teacher, lesson_slot=lessonslot)
            except TimetabledLesson.DoesNotExist:
                timetabledlesson = "FREE"
            currentday.append(timetabledlesson)
        weekgrid.append(currentday)

    return render(request, 'timetable/splash.html', {'weekgrid': weekgrid})


def classgroup_lesson_list(request, classgroup_pk):
    """Find all lessons for a given class group"""

    classgroup = ClassGroup.objects.get_or_create(pk=classgroup_pk)
    lessons = Lesson.objects.filter(lesson__classgroup=classgroup).order_by('date')

    return render(request, 'timetable/classgroup_lesson_list.html', {'lessons': lessons})
