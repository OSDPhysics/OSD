from django.forms import ModelForm
from teachnet.models import Objective, Skill


# Create the form class.
class ObjectiveForm(ModelForm):
    # TODO: Lock input to selected user ONLY
    class Meta:
        model = Objective
        fields = ['short_name', 'long_text']

