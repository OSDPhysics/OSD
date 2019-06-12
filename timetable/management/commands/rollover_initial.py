from django.core.management.base import BaseCommand
from school.models import ClassGroup
from tracker.models import Sitting


class Command(BaseCommand):
    help = "Roll students from old classgroups into their new rollover classgroups"

    def handle(self, *args, **options):
        classgroups = ClassGroup.objects. \
            filter(archived=False,
                   rollover_classgroup__isnull=False)

        for old_classgroup in classgroups:
            new_classgroup = old_classgroup.rollover_classgroup
            students = old_classgroup.students().all()
            for student in students:
                student.classgroups.add(new_classgroup)

        self.stdout.write(self.style.SUCCESS('Copied students from old classgroups to new'))
