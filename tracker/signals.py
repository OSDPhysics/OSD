from tracker.models import Mark
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=Mark)
def update_rating(sender, instance, **kwargs):

    points = instance.question.syllabuspoint.all()
    for point in points:
        rating = point.calculate_student_rating(instance.student)

