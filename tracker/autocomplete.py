from dal import autocomplete
from tracker.models import SyllabusPoint, Syllabus, Exam
from school.models  import ClassGroup


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
            qs = qs.filter(syllabusText__contains=self.q)

        return qs


class SyllabusPointAutocomplete2(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated:
            return SyllabusPoint.objects.none()
        qs = SyllabusPoint.objects.all()
        syllabus_pk = self.forwarded.get('syllabus', None)
        syllabus = Syllabus.objects.get(pk=syllabus_pk)

        if syllabus:
            qs = qs.filter(topic__syllabus=syllabus)

        if self.q:
            qs = qs.filter(syllabusText__contains=self.q)

        return qs


class ClaassgroupAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated:
            return ClassGroup.objects.none()

        qs = ClassGroup.objects.all()

        if self.q:
            qs = qs.filter(syllabusText__contains=self.q)

        return qs


class SyllabusAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Syllabus.objects.none()

        qs = Syllabus.objects.all()



        if self.q:
            qs = qs.filter(syllabusname__contains=self.q)

        return qs


