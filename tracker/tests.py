from django.test import TestCase
from tracker.models import MPTTSyllabus
# Create your tests here.

def createSimpleSyllabus():
    top, created = MPTTSyllabus.objects.get_or_create(text='S1: Top Level')
    sibling, created = MPTTSyllabus.objects.get_or_create(text='S2: Top level')
    top_child, created = MPTTSyllabus.objects.get_or_create(text='S1: First Child',
                                            parent=top)
    sibling_child, created = MPTTSyllabus.objects.get_or_create(text='S2: First Child',
                                                parent=sibling)


class SyllabusCheck(TestCase):
    def setUp(self):
        createSimpleSyllabus()

    def test_get_descendants(self):
        """ Name prints as expected """
        """ Family tree reports all items. """
        top = MPTTSyllabus.objects.get(text='S1: Top Level')
        tree = top.get_descendants(include_self=True)
        expected = MPTTSyllabus.objects.filter(text__contains='S1')

        self.assertQuerysetEqual(tree, map(repr, expected))


    def test_get_siblings(self):
        """ Check that the MPTT works for getting siblings"""
        top = MPTTSyllabus.objects.get(text='S1: Top Level')
        family = top.get_siblings(include_self=True)
        expected = MPTTSyllabus.objects.filter(text__contains="Top")
        self.assertQuerysetEqual(family, map(repr, expected))

    def test_calculate_ratings(self):
        pass
