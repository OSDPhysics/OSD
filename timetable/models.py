from django.db import models, IntegrityError
from django.shortcuts import reverse
from school.models import ClassGroup, Teacher
from tracker.models import SyllabusPoint, Syllabus, MPTTSyllabus
from osd.settings.base import CALENDAR_START_DATE, CALENDAR_END_DATE
from django.db import transaction
from django.contrib import messages
from django.db.models import Max
from mptt.models import TreeManyToManyField
from django.db.models import Max
from .functions import get_monday_date_from_weekno
# from .functions import *

import datetime

# Create your models here.

DAYS = (
    ('Monday', 'Monday'),
    ('Tuesday', 'Tuesday'),
    ('Wednesday', 'Wednesday'),
    ('Thursday', 'Thursday'),
    ('Friday', 'Friday'),
)

PERIODS = (
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
)

RESOURCE_TYPES = (
    ('Presentation', 'Presentation'),
    ('Worksheet', 'Worksheet'),
    ('Test', 'Test'),
    ('Mark Scheme', 'Mark Scheme'),
    ('Web Page', 'Web Page'),
    ('Google Drive', 'Google Drive'),
)


def get_year_from_date(date):
    for n in range(len(CALENDAR_START_DATE)):
        if CALENDAR_START_DATE[n] <= date <= CALENDAR_END_DATE[n]:
            return n
    # we'll only reach this if no date matches; this occurs
    # in the gap between school years.
    return len(CALENDAR_START_DATE) - 1  # since lists start at 0 and len is an absolute number!


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
                    lesson, created = Lesson.objects.get_or_create(lessonslot=timetabled_lesson, date=current_date)
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

    # Check if whole school is suspended that period
    suspensions = day_suspensions.filter(period=period, whole_school=True).count()
    if suspensions:
        return True

    # check if classgroup is suspended all day
    suspensions = day_suspensions.filter(all_day=True, classgroups=classgroup).count()
    if suspensions:
        return True

    # Check if classgroup is suspended for that period.
    suspensions = day_suspensions.filter(period=period, classgroups=classgroup).count()
    if suspensions:
        return True

    return False


class LessonSlot(models.Model):
    day = models.CharField(max_length=10, choices=DAYS, blank=False, null=False)
    period = models.IntegerField(choices=PERIODS, blank=False, null=False)
    year = models.IntegerField(blank=False, null=False)

    class Meta:
        unique_together = ['day', 'period', 'year']

    def __str__(self):
        return self.day + " P" + str(self.period) + " " + str(self.year)

    def dow(self):
        """Return the day of the week"""
        if self.day == "Monday":
            return 0
        if self.day == "Tuesday":
            return 1
        if self.day == "Wednesday":
            return 2
        if self.day == "Thursday":
            return 3
        if self.day == "Friday":
            return 4

    def teachers_lesson(self, teacher):
        """Return the TimetabledLesson assosciated with a teacher"""
        lesson = TimetabledLesson.objects.get(lesson_slot=self, classgroup__groupteacher=teacher)


class TimetabledLesson(models.Model):
    classgroup = models.ForeignKey(ClassGroup, on_delete=models.CASCADE, blank=True, null=True)
    lesson_slot = models.ForeignKey(LessonSlot, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        unique_together = ['classgroup', 'lesson_slot']

    def __str__(self):
        return str(self.classgroup) + " " + str(self.lesson_slot)

    def dow(self):
        return self.lesson_slot.day

    def total_lessons(self):
        lessons = int(TimetabledLesson.objects.filter(classgroup=self.classgroup).count())
        return lessons

    def order(self):
        all_instances = TimetabledLesson.objects.filter(classgroup=self.classgroup)
        return list(all_instances).index(self) + 1


class Lesson(models.Model):
    lessonslot = models.ForeignKey(TimetabledLesson, on_delete=models.CASCADE)
    classgroup = models.ForeignKey(ClassGroup, null=True, blank=False, on_delete=models.SET_NULL)
    status = models.CharField(max_length=20, null=True, blank=True)
    syllabus_points_covered = models.ManyToManyField(SyllabusPoint, blank=True)
    lesson_title = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    requirements = models.TextField(null=True, blank=True)
    homework = models.TextField(null=True, blank=True)
    homework_due = models.DateField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)

    sequence = models.IntegerField(null=False, blank=True)
    date = models.DateField(null=True, blank=True)
    syllabus = models.ForeignKey(Syllabus, blank=True, null=True, on_delete=models.SET_NULL)
    mptt_syllabus_points = TreeManyToManyField(MPTTSyllabus, blank=True)

    class Meta:
        unique_together = (("lessonslot", "date"),
                           ("classgroup", "sequence"))

    def __str__(self):
        if self.lesson_title:
            return str(self.classgroup) + " " + str(self.sequence) + ": " + str(self.lesson_title)

        else:
            return str(self.classgroup) + "lesson:  " + str(self.sequence) + " " + str(self.date)

    def resources(self):

        return LessonResources.objects.filter(lesson=self)

    def student_viewable_resources(self):
        # Get the resources set to be viewable at any time
        all_resources = []
        resources = LessonResources.objects.filter(lesson=self, students_can_view_before=True)
        print(all_resources)
        for resource in resources:
            all_resources.append(resource)

        # If it's been taught, get the 'after' resources:

        if self.date < datetime.date.today():
            resources = LessonResources.objects.filter(lesson=self, students_can_view_after=True).exclude(
                students_can_view_before=True)
            for resource in resources:
                all_resources.append(resource)

        return all_resources

    def set_date(self, year):

        """ A slightly complicated method, which must set the date for the current lesson.

        We need to create every lesson for the year.
         1. Set a start date + period
         2. Check if a lesson is suspended
         3. If not suspended, get_or_create the lesson, and set it to the date and period
         4. Move to next eligible lesson and repeat.

         """

        all_lessons = Lesson.objects.filter(lessonslot__classgroup=self.lessonslot.classgroup).order_by('sequence')

        # Lesson slots where these appear.
        slots = TimetabledLesson.objects.filter(classgroup=self.lessonslot.classgroup)

        # Find total lessons per week
        lessons_per_week = int(TimetabledLesson.objects.filter(classgroup=self.lessonslot.classgroup).count())

        # we'll use *week* to track each week we're looking at.

        global week, lesson_of_week, slot_number, current_lesson
        week = 0
        lesson_of_week = 0
        slot_number = 0
        current_lesson = 0
        # Set our starting lesson date:

        dow = slots[0].lesson_slot.dow()
        date = CALENDAR_START_DATE[year] + datetime.timedelta(days=dow)

        days_taught = []
        for slot in slots:
            days_taught.append(slot.lesson_slot.dow())

        def next_lesson(week, lesson_of_week, slot_number):
            if lesson_of_week == (lessons_per_week - 1):  # We just did the last lesson of the week
                week = week + 1
                lesson_of_week = 0

            else:
                lesson_of_week = lesson_of_week + 1

            if slot_number != lessons_per_week - 1:
                slot_number = slot_number + 1

            else:
                slot_number = 0

            date = CALENDAR_START_DATE + datetime.timedelta(days=days_taught[slot_number], weeks=week)

            return week, lesson_of_week, slot_number, date

        while date < CALENDAR_END_DATE[year]:

            # Iteratete this over the slots:

            for slot in slots:
                if check_suspension(date, slot.lesson_slot.period, slot.classgroup):
                    # lesson has been suspended
                    week, lesson_of_week, slot_number, date = next_lesson(week, lesson_of_week, slot_number)
                    continue

                else:  # lesson is not suspended
                    lesson, created = Lesson.objects.get_or_create(date=date, lessonslot=slots[slot_number],
                                                                   classgroup=slots[slot_number].classgroup)
                    # lesson.sequence = current_lesson
                    # current_lesson = current_lesson + 1
                    week, lesson_of_week, slot_number, date = next_lesson(week, lesson_of_week, slot_number)
                    lesson.save

    # def save(self, *args, **kwargs):
    #
    #     super(Lesson, self).save(*args, **kwargs)
    #
    #     return self

    def lesson_resource_icons(self):
        icons = []
        resources = LessonResources.objects.filter(lesson=self)

        for resource in resources:
            icons.append(resource.icon)

        return icons

    def delete(self, *args, **kwargs):
        # We've removed a lesson, so we need to decerement all the following lessons
        following_lessons = Lesson.objects.filter(classgroup=self.classgroup, sequence__gt=self.sequence).order_by(
            'sequence')
        # Avoid integrity error:
        # Find max sequence
        max = following_lessons.aggregate(Max('sequence'))

        if max['sequence__max'] is not None:
            self.sequence = max['sequence__max'] + 10
            self.save()
            for lesson in following_lessons:
                lesson.sequence = lesson.sequence - 1
                lesson.save()
        super().delete(*args, **kwargs)

    def homework_due_lessons(self):
        lessons_w_homework_due = Lesson.objects.filter(homework_due=self.date, classgroup=self.classgroup)
        if lessons_w_homework_due.count():
            return lessons_w_homework_due

        else:
            return False

    def next_in_order(self):
        return Lesson.objects.get(classgroup=self.classgroup,
                                  sequence=self.sequence + 1)


class LessonResources(models.Model):
    lesson = models.ForeignKey(Lesson, blank=True, null=True, on_delete=models.SET_NULL)
    resource_type = models.CharField(max_length=100, choices=RESOURCE_TYPES, null=True, blank=False)
    resource_name = models.CharField(max_length=100, null=True, blank=False)
    link = models.URLField(blank=False, null=True)
    students_can_view_before = models.BooleanField(default=False)
    students_can_view_after = models.BooleanField(default=False)
    available_to_all_classgroups = models.BooleanField(default=False)
    syllabus_points = models.ManyToManyField(SyllabusPoint, blank=True)
    mptt_syllabus_points = TreeManyToManyField(MPTTSyllabus)

    def __str__(self):
        return self.resource_name

    def editable_icon(self):
        """Link to the form to edit a resource """
        string = "<a href=" + str(reverse('timetable:edit_lesson_resource', args=[self.lesson.pk, self.pk]))
        string = string + ' target="_blank" data-toggle="tooltip" data-placement="top" title="'
        string = string + (str(self.resource_name))
        string = string + '">'

        if self.resource_type == "Presentation":
            string = string + "<i class='fas fa-desktop'>"

        elif self.resource_type == "Web Page":
            string = string + "<i class='fas fa-tablet-alt'>"

        elif self.resource_type == "Worksheet":
            string = string + '<i class="fas fa-newspaper">'

        elif self.resource_type == "Test":
            string = string + "<i class='fas fa-pencil-ruler'>"

        elif self.resource_type == "Google Drive":
            string = string + '<i class="fab fa-google-drive">'

        else:
            string = string + '<i class="fas fa-question-circle">'

        string = string + "</i></a>"

        return string


    def icon(self):
        """ Icon link to the resource itself"""

        string = "<a href=" + str(self.link)
        string = string + ' target="_blank" rel="noopener" data-toggle="tooltip" data-placement="top" title="'
        string = string + (str(self.resource_name))
        string = string + '">'

        if self.resource_type == "Presentation":
            string = string + "<i class='fas fa-desktop'>"

        elif self.resource_type == "Web Page":
            string = string + "<i class='fas fa-tablet-alt'>"

        elif self.resource_type == "Worksheet":
            string = string + '<i class="fas fa-newspaper">'

        elif self.resource_type == "Test":
            string = string + "<i class='fas fa-pencil-ruler'></i>"

        elif self.resource_type == "Google Drive":
            string = string + '<i class="fab fa-google-drive">'

        else:
            string = string + '<i class="fas fa-question-circle">'

        string = string + "</i></a>"

        return string

    def student_viewable(self):
        """ Return True if students should be able to see this resource """
        if self.students_can_view_before:
            return True

        elif self.students_can_view_after:
            if self.lesson.date >= datetime.date.today():
                return True

        else:
            return False

    def set_syllabus_points(self):
        if self.lesson:
            points = self.lesson.mptt_syllabus_points.all().order_by('pk')
            for point in points:
                self.mptt_syllabus_points.add(point)


class LessonSuspension(models.Model):
    """Store suspensions and missing lessons"""
    whole_school = models.BooleanField(default=True)
    date = models.DateField(blank=False, null=False)
    reason = models.CharField(max_length=200, blank=False, null=True)
    classgroups = models.ManyToManyField(ClassGroup, blank=True)
    all_day = models.BooleanField(default=False)
    period = models.IntegerField(choices=PERIODS, blank=True, null=True)

    def save(self, *args, **kwargs):
        """When we save, we need to update the dates of all affected lessons. """
        super(LessonSuspension, self).save(*args, **kwargs)

        affected_lessons = Lesson.objects.filter(date=self.date)
        for lesson in affected_lessons:
            classgroup = lesson.classgroup
            year = get_year_from_date(self.date)
            set_classgroups_lesson_dates(classgroup)

        return self

    def __str__(self):
        return str(self.date) + " " + self.reason


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
    # slots must be ordered for it to work - weirdly this doesn't happen on local!
    slots = TimetabledLesson.objects.filter(classgroup=classgroup).order_by('lesson_slot')
    year = classgroup.year_taught

    total_slots = slots.count() - 1  # index 0

    current_week = 0
    current_slot = 0
    current_lesson = 0

    message = False  # Used to return a warning message if lessons overshoot end date

    def next_lesson(current_slot, current_week, reset=False):
        if current_slot == total_slots:
            # Occurs if the last slot we filled was the last of the weeek
            current_slot = 0
            current_week = current_week + 1

        else:
            current_slot = current_slot + 1

        if reset:
            current_slot = 0
            current_week = 0

        return current_slot, current_week

    date = CALENDAR_START_DATE[year]
    # We start at the beginning of the school year
    current_week, current_slot = next_lesson(current_week, current_slot, True)

    while date < CALENDAR_END_DATE[year]:
        # We need to check if the lesson exists:

        try:
            lesson = Lesson.objects.get(sequence=current_lesson, classgroup=classgroup)
        except models.ObjectDoesNotExist:
            lesson = Lesson.objects.create(sequence=current_lesson, classgroup=classgroup,
                                           lessonslot=slots[current_slot])

        date = CALENDAR_START_DATE[year] + datetime.timedelta(weeks=current_week,
                                                              days=slots[current_slot].lesson_slot.dow())

        period = slots[current_slot].lesson_slot.period

        while True:
            # We need to keep trying with this period until we place it
            if check_suspension(date, period, classgroup):
                # lesson is suspended, so skip
                current_slot, current_week = next_lesson(current_slot, current_week)
                date = CALENDAR_START_DATE[year] + datetime.timedelta(weeks=current_week,
                                                                      days=slots[current_slot].lesson_slot.dow())
                continue  # Go back to the start and try again
            else:

                lesson.lessonslot = slots[current_slot]
                lesson.date = date
                current_slot, current_week = next_lesson(current_slot, current_week)

                # Check if a lesson already exists that meets all these criteria:

                try:
                    with transaction.atomic():  # Needed to prevent an error as per https://stackoverflow.com/questions/32205220/cant-execute-queries-until-end-of-atomic-block-in-my-data-migration-on-django-1?rq=1

                        lesson.save()  # Will fail if a lesson already has same date and slot

                except IntegrityError:
                    # All lessons above <current_sequence> must be incremented
                    clashing_lessons = Lesson.objects.filter(sequence__gte=current_lesson,
                                                             classgroup=classgroup).order_by('sequence').reverse()
                    # Must be in reverse order so we don't cause further integrity errors
                    # Note that we don't need to worry about setting correct slots here, as they are about to be re-set
                    for clashing_lesson in clashing_lessons:

                        # clashing_lesson.sequence = clashing_lesson.sequence + 1
                        # This date thing is a horrid hack, but we're about to set a correct date,
                        # and we need to make sure we don't cause further integrity errors

                        # temp bugxix:
                        if clashing_lesson.date:
                            clashing_lesson.date = clashing_lesson.date + datetime.timedelta(weeks=1000)
                        else:
                            clashing_lesson.date = CALENDAR_START_DATE[year] + datetime.timedelta(weeks=1000)
                        clashing_lesson.save()
                    lesson.save()  # Finally save our original lesson

                break  # End loop and get next lesson

        current_lesson = current_lesson + 1

    # re-set our values back to zero for next iteration (why???)

    next_lesson(current_week, current_slot, True)

    # clean up any lessons beyond end date
    overshot_lessons = Lesson.objects.filter(date__gte=CALENDAR_END_DATE[year], classgroup=lesson.classgroup)

    # Delete only unwritten lessons
    overshot_lessons.filter(lesson_title__isnull=True).delete()

    # Check if any are left - this means that some had titles
    if Lesson.objects.filter(date__gte=CALENDAR_END_DATE[year], classgroup=lesson.classgroup).count():
        message = "Warning! Your scheduled lessons extend beyond the last day of term."

    return message
