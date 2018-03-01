from django.contrib.auth.models import User
from models import Student
import csv
import codecs

def processstudentcsv(csvfile):
    dialect = csv.Sniffer().sniff(codecs.EncodedFile(csvfile, "utf-8").read(1024))
    csvfile.open()
    reader = csv.reader(codecs.EncodedFile(csvfile, "utf-8"), delimiter=',', dialect=dialect)
        for row in reader
            newstudent = {}
            newstudent['last_name'] = row[0]
            newstudent['first_name'] = row[1]
            newstudent['Gender'] = row[3]
            newstudent['email'] = row[4]
            newstudent['username'] = row[5]
            newstudent['studentid'] = row[6]
            newstudent['password'] = row[6]
            newstudent['class'] = row[7]

            addstudent(newstudent)

def addstudent(newstudent):

    user = User.objects.create_user(username="newstudent['username']",
                                 email="newstudent['email']",
                                 password="newstudent['password']",
                                 first_name="newstudent['last_name']",
                                 last_name="newstudent['first_name']"
                                 )
    student = Students.objects.create(username.pk=user,
                                    Gender="newstudent['Gender']",
                                    studentid="newstudent['studentid'] = row[6]"
                                    
                                    )
