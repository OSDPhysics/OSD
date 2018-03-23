# Generated by Django 2.0.1 on 2018-03-23 00:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Examboard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('board', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Examlevel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('examtype', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Mark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qnumber', models.CharField(max_length=100)),
                ('qorder', models.IntegerField()),
                ('maxscore', models.IntegerField()),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracker.Exam')),
            ],
        ),
        migrations.CreateModel(
            name='Syllabus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('syllabusname', models.CharField(max_length=50)),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracker.Examboard')),
                ('examtype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracker.Examlevel')),
            ],
        ),
        migrations.CreateModel(
            name='SyllabusPoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(blank=True, max_length=10, null=True)),
                ('syllabusText', models.TextField(blank=True, null=True)),
                ('syllabusLevel', models.CharField(blank=True, choices=[('core', 'core'), ('extended', 'extended')], max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SyllabusTopic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(blank=True, max_length=100, null=True)),
                ('syllabus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracker.Syllabus')),
            ],
        ),
        migrations.AddField(
            model_name='syllabuspoint',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracker.SyllabusTopic'),
        ),
        migrations.AddField(
            model_name='question',
            name='syllabuspoint',
            field=models.ManyToManyField(blank=True, to='tracker.SyllabusPoint'),
        ),
        migrations.AddField(
            model_name='mark',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracker.Question'),
        ),
        migrations.AddField(
            model_name='mark',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.Student'),
        ),
        migrations.AddField(
            model_name='exam',
            name='syllabus',
            field=models.ManyToManyField(to='tracker.Syllabus'),
        ),
    ]
