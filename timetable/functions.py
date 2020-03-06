import datetime
from osd.settings.base import CALENDAR_END_DATE, CALENDAR_START_DATE, CALENDAR_TOTAL_WEEKS

def get_monday_date_from_weekno(week_number, year):
    start_date = CALENDAR_START_DATE[year] + datetime.timedelta(weeks=week_number)
    return start_date


def get_weekno_from_date(date, year):

    start_year = CALENDAR_START_DATE[year].isocalendar()[0]
    date_year = date.isocalendar()[0]

    # Find week of the year

    date_week = datetime.datetime.now().isocalendar()[1]
    start_week = CALENDAR_START_DATE[year].isocalendar()[1]
    week_number = date_week - start_week

    # This is to default to 0 before the school year starts.
    if week_number < 0:
        if start_year == date_year:
            return 0
        # This is necessary for school years which span calendar years.
        else:
            last_day_of_year = datetime.date(start_year, 12, 24)
            #last_week_of_year = last_day_of_year.isocalendar()[1] # Sometimes there are 53 weeks in a year
            last_week_of_year = 52 # Not sure if this is correct or the previous should be used
            final_timetable_week = last_week_of_year - start_week

            return final_timetable_week + date_week

    else:
        return date_week - start_week


def get_next_tt_week_year(week, year):
    week = week + 1
    if get_monday_date_from_weekno(week, year) < CALENDAR_END_DATE[year]:
        return week, year
    else:
        return 0, year + 1


def get_previous_tt_week_year(week, year):
    week = week - 1
    if get_monday_date_from_weekno(week, year) > CALENDAR_START_DATE[year]:
        return week, year
    else:
        return int(CALENDAR_TOTAL_WEEKS[year - 1]), year - 1


def check_suspension(date, period, classgroup):
    # Check if the whole school is suspended that day:
    from timetable.models import LessonSuspension
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
    from timetable.models import Lesson, TimetabledLesson
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
    from school.models import ClassGroup
    from tracker.models import SyllabusPoint
    classgroups = ClassGroup.objects.all()
    for classgroup in classgroups:
        students = classgroup.students().all()
        syllabus = classgroup.syllabustaught.all()
        points = SyllabusPoint.objects.filter(topic__syllabus__classgroup=classgroup)
        for student in students:
            for point in points:
                point.calculate_student_rating(student)
