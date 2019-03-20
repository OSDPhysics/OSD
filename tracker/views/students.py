from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from tracker.forms import *
from tracker.charts import CohortPointGraph, CohortSubTopicChart, StudentChart, StudentSubTopicGraph
from journal.forms import StudentJournalEntryLarge
from journal.functions import move_mark_reflection_to_journal_student_mptt
from osd.decorators import *
from django.urls import reverse, reverse_lazy
from journal.models import StudentJournalEntry
from django.contrib import messages
from timetable.models import Lesson, LessonResources
from school.models import PastoralStructure, AcademicStructure
from django.db.models import Sum
from operator import itemgetter
import datetime

from tracker.models import *
import logging
from tracker.functions.adddata import *
import os

logger = logging.getLogger(__name__)