# Generated by Django 2.1.7 on 2019-03-12 05:01

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0006_auto_20190312_1301'),
        ('school', '0003_auto_20190311_1441'),
    ]

    operations = [
        migrations.CreateModel(
            name='AcademicStructure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('kpis', models.ManyToManyField(to='tracker.StandardisedData')),
                ('leaders', models.ManyToManyField(to='school.Teacher')),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='school.AcademicStructure')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PastoralStructure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('kpis', models.ManyToManyField(to='tracker.StandardisedData')),
                ('leaders', models.ManyToManyField(to='school.Teacher')),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='school.PastoralStructure')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='department',
            name='faculty',
        ),
        migrations.RemoveField(
            model_name='department',
            name='leaders',
        ),
        migrations.RemoveField(
            model_name='faculty',
            name='leaders',
        ),
        migrations.RemoveField(
            model_name='keystage',
            name='leaders',
        ),
        migrations.RemoveField(
            model_name='keystage',
            name='phase',
        ),
        migrations.RemoveField(
            model_name='phase',
            name='leaders',
        ),
        migrations.RemoveField(
            model_name='yeargroup',
            name='key_stage',
        ),
        migrations.RemoveField(
            model_name='yeargroup',
            name='leaders',
        ),
        migrations.DeleteModel(
            name='Department',
        ),
        migrations.DeleteModel(
            name='Faculty',
        ),
        migrations.DeleteModel(
            name='KeyStage',
        ),
        migrations.DeleteModel(
            name='Phase',
        ),
        migrations.DeleteModel(
            name='YearGroup',
        ),
    ]
