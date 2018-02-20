import os
import csv

from django.core.management.base import BaseCommand, CommandError
from django.db.models.loading import get_model

class Command(BaseCommand):
    args = 'students.csv'
    help = 'Import `Model`.csv into `Model` database.'

    def handle(self, *args, **options):
        if len(args) != 1:
            raise CommandError ("Invalid Invocation. See help.")

        csvPath = args[0]
        if not os.path.exists (csvPath):
            raise CommandError ("%s doesnt exist." %csvPath)

        model, _ = os.path.splitext (os.path.basename(csvPath))
        Model = get_model ("Student", model.title ())
        if not Model:
            raise CommandError ("%s Model doesn't exist'")

        model_fields = [f.name for f in Model._meta.fields]
        fields_name = []
        with open (csvPath, 'rb') as csvFile:
            reader = csv.reader (csvFile, delimiter=',', quotechar="\"")
            fields_name = reader.next ()
            for i, _ in enumerate(fields_name):
                fields_name[i] = fields_name[i].lower ()
                fields_name[i] = fields_name[i].replace (' ', '_')
                if not fields_name[i] in model_fields:
                    raise CommandError ("%s field doesn't exists in %s Model" %(fields_name[i], Model))

            for row in reader:
                try:
                    obj = Model()
                    for i, field in enumerate(row):
                        setattr (obj, fields_name[i], field)
                    obj.save ()
                except Exception,e:
                    raise CommandError(e)
