from timetable.models import *
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
                    weekgrid.append([day[0], suspension, suspension, suspension, suspension])
                    current_date = current_date + datetime.timedelta(days=1)
                    continue

        dayrow = [day[0]]

        for period in PERIODS:
            # Check if that period is whole-school suspended:
            check = suspensions.filter(period=period[0]).filter(whole_school=True)
            if check.exists():
                dayrow.append(check[0])  # See above: May like to change to a get.
                current_date = current_date + datetime.timedelta(days=1)
                continue

            try:

                # Check the timetable to see if the lesson actually exists
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
                    lesson, created = Lesson.objects.get(lessonslot=timetabled_lesson,
                                                         date=current_date,
                                                         classgroup=timetabled_lesson.classgroup)
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


def set_classgroups_lesson_dates(classgroup):
    lessons = Lesson.objects.filter(classgroup=classgroup).order_by("sequence")

    slots = TimetabledLesson.objects.filter(classgroup=classgroup)

    global total_slots, current_week, current_slot

    total_slots = slots.count() - 1

    current_week = 0
    current_slot = 0

    def next_lesson(current_slot, current_week):
        if current_slot == total_slots:
            current_slot = 0
            current_week = current_week + 1

        else:
            current_slot = current_slot + 1

        return current_slot, current_week

    for lesson in lessons:
        date = CALENDAR_START_DATE + datetime.timedelta(weeks=current_week, days=lesson.lessonslot.lesson_slot.dow())
        period = slots[current_slot].lesson_slot.period

        while True:
            # We need to keep trying with this period until we place it
            if check_suspension(date, period, classgroup):
                # lesson is suspended, so skip
                current_slot, current_week = next_lesson(current_slot, current_week)
                continue  # Go back to the start and try again
            else:

                lesson.lessonslot = slots[current_slot]
                lesson.date = date
                current_slot, current_week = next_lesson(current_slot, current_week)
                lesson.save(date_to_set=date)
                break  # End loop and get next lesson


def set_initial_current_calculated():
    classgroups = ClassGroup.objects.all()
    for classgroup in classgroups:
        students = classgroup.students().all()
        syllabus = classgroup.syllabustaught.all()
        points = SyllabusPoint.objects.filter(topic__syllabus__classgroup=classgroup)
        for student in students:
            for point in points:
                point.calculate_student_rating(student)
