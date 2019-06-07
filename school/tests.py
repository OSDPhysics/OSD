from django.test import TestCase
from django.contrib.auth.models import User
from school.models import Teacher, ClassGroup
from tracker.models import MPTTSyllabus

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


def setUpSyllabus():
    top_level = MPTTSyllabus.objects.create()


class TeacherTestCase(TestCase):
    def setUp(self):
        teacher = setUpTeacher()

    def test_correct_display_name(self):
        """ Name prints as expected """
        teacher = Teacher.objects.get(staffcode='TEST')
        self.assertEqual(str(teacher), 'Mr Test teacher (TEST)')


class ClassGroupTestCase(TestCase):
    def setUp(sefl):
        teacher = setUpTeacher()

