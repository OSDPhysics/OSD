# Generated by Django 2.2.4 on 2019-08-30 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0010_remove_homework_links'),
    ]

    operations = [
        migrations.AddField(
            model_name='lessonresources',
            name='lessons',
            field=models.ManyToManyField(blank=True, related_name='Lesson2', to='timetable.Lesson'),
        ),
    ]
