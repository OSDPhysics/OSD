from django.contrib import admin

# Register your models here.

from .models import Teacher
from .models import TutorGroup
from .models import ClassGroup
from. models import Student
from .models import Exam
from .models import Question
from .models import *


admin.site.register(Teacher)
admin.site.register(TutorGroup)
admin.site.register(ClassGroup)
admin.site.register(Student)
admin.site.register(Exam)
admin.site.register(Question)
admin.site.register(Examboard)
admin.site.register(Examlevel)
admin.site.register(Syllabus)
admin.site.register(Syllabuspoint)
