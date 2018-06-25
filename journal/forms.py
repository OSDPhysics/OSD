from django.forms import ModelForm
from journal.models import StudentJournalEntry
from ckeditor.widgets import CKEditorWidget

class StudentJournalExisting(ModelForm):
    class Meta:
        model = StudentJournalEntry
        fields = ['entry']


class StudentJournalEntryLarge(ModelForm):
    class Meta:
        model = StudentJournalEntry
        fields = ['entry']
        widgets = {'entry': CKEditorWidget(config_name='large')}
