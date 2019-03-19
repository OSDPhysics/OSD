# Generated by Django 2.1.7 on 2019-03-19 02:25

from django.db import migrations

def link_targets_and_data(apps, schema_editor):
    StandardisedResult = apps.get_model('tracker', 'StandardisedResult')

    results = StandardisedResult.objects.filter(result__isnull=False)

    for result in results:
        result.save()

class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0021_auto_20190319_0756'),
    ]

    operations = [
        migrations.RunPython(link_targets_and_data)
    ]
