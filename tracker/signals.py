from tracker.models import Mark, StudentPointRating, Exam, Question, SyllabusPoint
from school.models import Student
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=Mark)
def update_rating_after_mark_change(sender, instance, **kwargs):
    """ This needs to be run as we've changed a mark """
    # TODO: Remove when no longer using calculated ratings
    student = instance.student
    question = instance.question
    points = question.syllabuspoint.all()

    for point in points:
        point.calculate_student_rating(student)

@receiver(post_save, sender=Mark)
def calculate_percent_after_save(sender, instance, **kwargs):
    percent = instance.calculate_percentage()
    if percent != instance.percent:
        instance.percent = percent
        instance.save()


@receiver(post_save, sender=Mark)
def calculate_weighted(sender, instance, **kwargs):
    percent = instance.calculate_percentage()
    if percent != instance.percent:
        instance.percent = percent
        instance.save()


@receiver(post_save, sender=Mark)
def add_max_after_save(sender, instance, **kwargs):
    max = instance.question.maxscore
    if instance.maximum != max:
        instance.maximum = max
        instance.save()


@receiver(post_save, sender=Mark)
def save_weighted_percent(sender, instance, **kwargs):
    if not instance.weighted_max:
        instance.weighted_max = instance.calculate_weighted_max()

    calculated_weighted_percent = instance.calculate_weighted_percent

    if instance.weighted_percent != calculated_weighted_percent:
        instance.weighted_perent = calculated_weighted_percent
        instance.save()


@receiver(post_save, sender=Mark)
def save_weighted_max(sender, instance, **kwargs):

    if instance.weighted_max != instance.calculate_weighted_max:
        instance.weighted_max = instance.calculate_weighted_max()
        instance.save()


@receiver(post_save, sender=Exam)
def update_rating_after_exam_change(sender, instance, **kwargs):
    """ This needs to be run in case we've added spec points. """
    students = Student.objects.filter(classgroups__sitting__exam=instance)
    points = SyllabusPoint.objects.filter(question__exam=instance)


@receiver(post_save, sender=Question)
def update_marks_after_q_save(sender, instance, **kwargs):
    marks = Mark.objects.filter(question=instance)
    for mark in marks:
        mark.updates = mark.updates + 1
        mark.save()


@receiver(post_save, sender=Exam)
def update_marks_after_exam_save(sender, instance, **kwargs):
    marks = Mark.objects.filter(question__exam=instance)
    for mark in marks:
        mark.updates = mark.updates + 1
        mark.save()


@receiver(post_save, sender=StudentPointRating)
def update_current(sender, instance, **kwargs):

    # Check if the just-saved rating is newer than the 'current' one:
    try:
        current = StudentPointRating.objects.filter(student=instance.student,
                                                 syllabus_point=instance.syllabus_point,
                                                 current=True)
        for x in current:
            if x.date < instance.date:
                x.current = False
                instance.current = True
                x.save()
                instance.save()


    except StudentPointRating.DoesNotExist:
        # This will occur if no object is set to be the current.
        instance.current = True
        instance.save()
