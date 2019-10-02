from django.core.management.base import BaseCommand
from school.models import ClassGroup
from timetable.models import get_year_from_date
from datetime import date
class Command(BaseCommand):
    help = "Archive old classes"

    def handle(self, *args, **options):
        current_year = get_year_from_date(date.today())
        old_classgroups = ClassGroup.objects.filter(year_taught__lt=current_year)
        for group in old_classgroups:
            group.archived = True
            group.save()
