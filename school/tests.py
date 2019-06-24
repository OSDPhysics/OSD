from django.test import TestCase
from django.contrib.auth.models import User
from school.models import Teacher, ClassGroup
from tracker.models import MPTTSyllabus
from tracker.tests import createSimpleSyllabus


# Create your tests here.

def setUpTeacher():
    user = User.objects.create(first_name='Test',
                               last_name='teacher',
                               email='test@example.com',
                               is_staff=True,
                               )
    teacher = Teacher.objects.create(user=user,
                                     title='Mr',
                                     staffcode='TEST',
                                     )

    return teacher


def setUpClassGroup():
    group, created = ClassGroup.objects. \
        get_or_create(groupname='Test Group',
                      defaults={
                          'groupteacher': setUpTeacher(),
                          'year_taught': 1})

    createSimpleSyllabus()

    syllabus = MPTTSyllabus.objects.get(text='S1: Top Level')
    group.mptt_syllabustaught.add(syllabus)
    return group


class TeacherTestCase(TestCase):
    def setUp(self):
        teacher = setUpTeacher()

    def test_correct_display_name(self):
        """ Name prints as expected """
        teacher = Teacher.objects.get(staffcode='TEST')
        self.assertEqual(str(teacher), 'Mr Test teacher (TEST)')


class ClassGroupTestCase(TestCase):
    def setUp(self):
        setUpClassGroup()

    def test_name(self):
        group = ClassGroup.objects.get(groupname='Test Group')
        self.assertEqual(str(group), 'Test Group 2019-20')
