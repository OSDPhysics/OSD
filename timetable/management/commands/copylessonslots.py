from django.core.management.base import BaseCommand
from timetable.models import LessonSlot


class Command(BaseCommand):
    help = "Roll over the last year's timetable"

    def handle(self, *args, **options):
        slots = LessonSlot.objects.all()
        for slot in slots:
            new = slot
            new.pk = None
            new.year = new.year + 1
            new.save()
        self.stdout.write(self.style.SUCCESS('Copied your lesson slots to next years'))
