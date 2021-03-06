# Generated by Django 2.2.4 on 2019-08-30 03:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0008_auto_20190612_1254'),
    ]

    operations = [
        migrations.CreateModel(
            name='Homework',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='lessonresources',
            name='resource_type',
            field=models.CharField(choices=[('Presentation', 'Presentation'), ('Worksheet', 'Worksheet'), ('Test', 'Test'), ('Mark Scheme', 'Mark Scheme'), ('Web Page', 'Web Page'), ('Google Drive', 'Google Drive')], max_length=100, null=True),
        ),
        migrations.CreateModel(
            name='SetHomework',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('due_date', models.DateField()),
                ('homework', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='timetable.Homework')),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='timetable.Lesson')),
            ],
        ),
        migrations.AddField(
            model_name='homework',
            name='links',
            field=models.ManyToManyField(blank=True, to='timetable.LessonResources'),
        ),
    ]
