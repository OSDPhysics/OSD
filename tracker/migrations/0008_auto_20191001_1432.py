# Generated by Django 2.2.4 on 2019-10-01 06:32

from django.db import migrations
# remove this later
#from tracker.models import MPTTSyllabus, Exam


def set_root_topic(apps, schema_editor):

    MPTTSyllabus = apps.get_model('tracker', 'MPTTSyllabus')
    Exam = apps.get_model('tracker', 'Exam')
    gis_home = MPTTSyllabus.objects.get(text__contains='Garden International')
    for exam in Exam.objects.all():
        exam.root_syllabus = gis_home
        exam.save()

class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0007_exam_root_syllabus'),
    ]

    operations = [
        migrations.RunPython(set_root_topic),
    ]