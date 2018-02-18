# Generated by Django 2.0.1 on 2018-02-17 10:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0008_auto_20180209_0430'),
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
            name='Syllabuspoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('syllabustext', models.CharField(max_length=500)),
                ('syllabus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracker.Syllabus')),
            ],
        ),
        migrations.AddField(
            model_name='mark',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracker.Question'),
        ),
        migrations.AddField(
            model_name='mark',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracker.Student'),
        ),
        migrations.AddField(
            model_name='exam',
            name='level',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracker.Examlevel'),
        ),
        migrations.AddField(
            model_name='exam',
            name='syllabus',
            field=models.ManyToManyField(to='tracker.Syllabus'),
        ),
    ]
