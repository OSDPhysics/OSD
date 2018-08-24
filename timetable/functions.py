from timetable.models import *
from django.db.models import Max
import datetime


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
                    weekgrid.append([day[0], suspension, suspension, suspension, suspension ])
                    current_date = current_date + datetime.timedelta(days=1)
                    continue

        dayrow = [day[0]]

        for period in PERIODS:
            # Check if that period is whole-school suspended:
            check = suspensions.filter(period=period[0]).filter(whole_school=True)
            if check.exists():
                dayrow.append(check[0]) # See above: May like to change to a get.
                current_date = current_date + datetime.timedelta(days=1)
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

                else:
                    lesson, created = Lesson.objects.get_or_create(lesson=timetabled_lesson, date=current_date)
                    dayrow.append(lesson)

        weekgrid.append(dayrow)
        current_date = current_date + datetime.timedelta(days=1)


    return weekgrid



