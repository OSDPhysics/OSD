from school.models import PastoralStructure, TutorGroup, Student, ClassGroup, AcademicStructure
import re

def create_pastoral_tgs():
    tutorgroups = TutorGroup.objects.all()
    for group in tutorgroups:
        year = re.search(r'\d+', group.tgname).group()
        parent = PastoralStructure.objects.get(name='Year ' + str(year))
        pastoral_group, created = PastoralStructure.objects.get_or_create(name=group.tgname,
                                                                          parent=parent)
        print("Currently on" + group.tgname)
        if group.tgtutor:
            pastoral_group.leaders.add(group.tgtutor)
            print("Added a tutor")


def add_student_pastoral_tgs():
    for student in Student.objects.filter(tutorgroup__isnull=False):
        if student.tutorgroup:
            student.academic_tutorgroup = PastoralStructure.objects.get(name=student.tutorgroup)
            student.save()


