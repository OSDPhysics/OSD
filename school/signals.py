from django.dispatch import receiver
from django.db.models.signals import post_migrate
from school.models import AcademicStructure

# Some migrations require us to create new MPTT objects.
# Since MPTTTreeManager is unavailable during during migrations,
# we must do this as a signal after migrations.

# See https://github.com/django-mptt/django-mptt/issues/382#issuecomment-136151904


@receiver(post_migrate)
def rebuild_handler(sender, **kwargs):
    # post_migrate is called after each app's migrations
    if sender.name == 'school':
        AcademicStructure.objects.rebuild()
