# Generated by Django 2.1.7 on 2019-06-03 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0006_auto_20190517_1642'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='SIMS_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='dob',
            field=models.DateField(blank=True, null=True),
        ),
    ]
