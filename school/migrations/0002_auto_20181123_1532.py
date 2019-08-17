# Generated by Django 2.0.1 on 2018-11-23 07:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('teachnet', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tracker', '0001_initial'),
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='skills',
            field=models.ManyToManyField(to='teachnet.Skill'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='student',
            name='classgroups',
            field=models.ManyToManyField(to='school.ClassGroup'),
        ),
        migrations.AddField(
            model_name='student',
            name='tutorgroup',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='school.TutorGroup'),
        ),
        migrations.AddField(
            model_name='student',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='classgroup',
            name='groupteacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.Teacher'),
        ),
        migrations.AddField(
            model_name='classgroup',
            name='syllabustaught',
            field=models.ManyToManyField(to='tracker.Syllabus'),
        ),
    ]
