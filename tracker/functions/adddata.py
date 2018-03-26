from django.contrib.auth.models import User
from tracker.models import *
import csv
import codecs


def processSpecification(path):
    with open(path, newline='') as csvfile:
        specification = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in specification:
            newSpecPoint = {}
            newSpecPoint['topic'] = row[0]
            newSpecPoint['number'] = row[1]
            newSpecPoint['text'] = row[2]
            newSpecPoint['level'] = row[3]

            addSpecPoint(newSpecPoint)


def addSpecPoint(newSpecPoint):
    topic = SyllabusTopic.objects.get(topic=newSpecPoint['topic'])

    specPoint = SyllabusPoint.objects.create(topic=topic,
                                             number=newSpecPoint['number'],
                                             syllabusText=newSpecPoint['text'],
                                             syllabusLevel=newSpecPoint['level'])

    return specPoint


