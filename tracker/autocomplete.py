from dal import autocomplete
from tracker.models import SyllabusPoint
from school.models  import ClassGroup


class SyllabusPointAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated:
            return SyllabusPoint.objects.none()

        qs = SyllabusPoint.objects.all()

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