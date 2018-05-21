from django.forms import ModelForm
from teachnet.models import Objective, Skill
from ckeditor.widgets import CKEditorWidget


# Create the form class.
class ObjectiveForm(ModelForm):
    # TODO: Lock input to selected user ONLY
    class Meta:
        model = Objective
        fields = ['short_name', 'long_text']
        widgets = {
            'long_text': CKEditorWidget(),
        }
