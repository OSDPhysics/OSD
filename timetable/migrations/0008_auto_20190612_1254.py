# Generated by Django 2.1.7 on 2019-06-12 04:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0007_auto_20190612_0953'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='lessonslot',
            unique_together={('day', 'period', 'year')},
        ),
    ]
