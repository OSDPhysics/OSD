# Generated by Django 2.0.1 on 2019-01-05 09:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0002_auto_20181125_2012'),
        ('timetable', '0002_auto_20181125_2012'),
    ]

    operations = [
        migrations.AddField(
            model_name='lessonresources',
            name='available_to_all_classgroups',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='lessonresources',
            name='syllabus_points',
            field=models.ManyToManyField(blank=True, to='tracker.SyllabusPoint'),
        ),
        migrations.AlterField(
            model_name='lessonresources',
            name='lesson',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='timetable.Lesson'),
        ),
        migrations.AlterField(
            model_name='lessonresources',
            name='link',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='lessonresources',
            name='resource_type',
            field=models.CharField(choices=[('Presentation', 'Presentation'), ('Worksheet', 'Worksheet'), ('Test', 'Test'), ('Mark Scheme', 'Mark Scheme'), ('Web Page', 'Web Page')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='lessonresources',
            name='students_can_view_after',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='lessonresources',
            name='students_can_view_before',
            field=models.BooleanField(default=False),
        ),
    ]