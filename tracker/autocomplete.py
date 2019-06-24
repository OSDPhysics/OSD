from dal import autocomplete
from tracker.models import SyllabusPoint, Syllabus, Exam, MPTTSyllabus
from school.models  import ClassGroup
from timetable.models import Lesson


class SyllabusPointAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated:
            return SyllabusPoint.objects.none()
        qs = SyllabusPoint.objects.all()
        exam_pk = self.forwarded.get('exam', None)
        exam = Exam.objects.get(pk=exam_pk)
        if exam:
            syllabus = exam.syllabus.all()
            qs = qs.filter(topic__syllabus__in=syllabus)

        if self.q:
            qs = qs.filter(syllabusText__icontains=self.q)

        return qs


class SyllabusPointAutocomplete2(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated:
            return SyllabusPoint.objects.none()
        qs = SyllabusPoint.objects.all()
        if self.forwarded.get('syllabus', None):
            syllabus_pk = self.forwarded.get('syllabus', None)
            syllabus = Syllabus.objects.get(pk=syllabus_pk)
            qs = qs.filter(topic__syllabus=syllabus)

        if self.q:
            qs = qs.filter(syllabusText__icontains=self.q)

        return qs

class MPTTSyllabusAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return MPTTSyllabus.objects.none()

        qs = MPTTSyllabus.objects.all()

        if self.forwarded.get('parent', None):
            parent_pk = self.forwarded.get('parent', None)
            parent = MPTTSyllabus.objects.get(pk=parent_pk)
            qs = parent.get_descendants()

        if self.q:
            qs = qs.filter(text__icontains=self.q)

        return qs

class ClaassgroupAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated:
            return ClassGroup.objects.none()

        qs = ClassGroup.objects.all()

        if self.forwarded.get('syllabus', None):
            syllabus_pk = self.forwarded.get('parent', None)
            qs = qs.filter(mptt_syllabustaught__pk=syllabus_pk)

        if self.forwarded.get('include_archived', None):
            qs.filter(archived=False)

        else:
            qs.filter(archived=True)

        if self.q:
            qs = qs.filter(groupname__icontains=self.q,
                           archived=False)

        return qs


class LessonAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated:
            return Lesson.objects.none()

        qs = Lesson.objects.all().order_by('date')

        if self.forwarded['classgroup']:
            qs = qs.filter(classgroup__pk=self.forwarded['classgroup'])

        if self.q:
            qs = qs.filter(date=self.q)

        return qs


class SyllabusAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Syllabus.objects.none()

        qs = Syllabus.objects.all()

        if self.q:
            qs = qs.filter(syllabusname__icontains=self.q)

        return qs


