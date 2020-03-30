from tracker.models import MPTTSyllabus
from django.http import JsonResponse


def MPTTSyllabusJson(request, parent_pk=MPTTSyllabus.objects.none()):
    parent = MPTTSyllabus.objects.get(pk=parent_pk)

    children = parent.get_children().values('text', 'pk', 'level')
    children_list = list(children)
    return JsonResponse(children_list, safe=False)
