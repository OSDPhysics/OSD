from bs4 import BeautifulSoup
import re
import sys, os, django
sys.path.append("/Users/wright.j/PycharmProjects/OSD/") #here store is root folder(means parent).
#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "osd.settings")
#django.setup()

from tracker.models import Student

htmlfilename = 'sampleHTML.html'


def getimageURLs(htmlfilename):
    with open(htmlfilename) as fp:
        soup = BeautifulSoup(fp, "html5lib")

    qpattern = re.compile(r'qbtn.*')
    test = soup.find_all(id=qpattern)

    imgpattern = re.compile(r'staging.*\.png')

    imglist = []

    for line in test:
        images = re.search(imgpattern,str(line)).group()
        individuals = images.split(',')

        for subline in individuals:
            imglist.append(subline)

    return imglist


for line in getimageURLs(htmlfilename):
    print line

print Student.objects.all()