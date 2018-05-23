from django.forms import ModelForm
from journal.models import StudentJournalEntry

class StudentJournalExisting(ModelForm):
    class Meta:
        model = StudentJournalEntry
        fields = ['entry']