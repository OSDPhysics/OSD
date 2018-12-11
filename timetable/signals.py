from timetable.models import LessonResources, Lesson
from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver


@receiver(m2m_changed, sender=Lesson.syllabus_points_covered.through)
def post_update_lesson_syllabus_pts(sender, instance, **kwargs):
    """ After adding a syllabus point to a lesson, update its resources"""
    resources = instance.resources()
    for resource in resources:
        resource.set_syllabus_points()


@receiver(post_save, sender=LessonResources)
def update_resources(sender, instance, **kwargs):
    """ After adding a resource, check its syllabus points match its lesson """
    print('Before set_syllabus_points')
    print(instance.pk)
    print(instance.syllabus_points.all())
    instance.set_syllabus_points()
    print('After set_syllabus_points')
    print(instance.syllabus_points.all())



