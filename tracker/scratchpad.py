/ Users / wright.j / django - test / bin / python / Applications / PyCharm.app / Contents / helpers / pydev / pydevconsole.py
60280
60281
import sys;

print('Python %s on %s' % (sys.version, sys.platform))
import django;

print('Django %s' % django.get_version())
sys.path.extend(['/Users/wright.j/PycharmProjects/OSD', '/Applications/PyCharm.app/Contents/helpers/pycharm',
                 '/Applications/PyCharm.app/Contents/helpers/pydev'])
if 'setup' in dir(django): django.setup()
import django_manage_shell;

django_manage_shell.run("/Users/wright.j/PycharmProjects/OSD")
PyDev
console: starting.
Python
3.6
.4(v3
.6
.4: d48ecebad5, Dec
18
2017, 21: 07:28)
[GCC 4.2.1(Apple Inc.build 5666) (dot 3)] on
darwin
Django
2.0
.1
from tracker.models import *

sitting = Sitting.objects.get(pk=2)
student = Student.objects.get(pk=34)
marks = Mark.objects.filter(sitting=sitting).filter(student=student).order_by('question__qorder')
MarkFormset = modelformset_factory(Mark, fields=('question', 'score'), extra=0)
formset = MarkFormset(
    queryset=Mark.objects.filter(sitting=sitting).filter(student=student).order_by('question__qorder'))
File
"<input>", line
2
formset = MarkFormset(
          ^
          IndentationError: unexpected
indent
MarkFormset = modelformset_factory(Mark, fields=('question', 'score'), extra=0)
formset = MarkFormset(
    queryset=Mark.objects.filter(sitting=sitting).filter(student=student).order_by('question__qorder'))
Traceback(most
recent
call
last):
File
"<input>", line
1, in < module >
        NameError: name
'modelformset_factory' is not defined
from django.forms import modelformset_factory

MarkFormset = modelformset_factory(Mark, fields=('question', 'score'), extra=0)
formset = MarkFormset(
    queryset=Mark.objects.filter(sitting=sitting).filter(student=student).order_by('question__qorder'))
formset.hiddenfields
Traceback(most
recent
call
last):
File
"<input>", line
1, in < module >
        AttributeError: 'MarkFormFormSet'
object
has
no
attribute
'hiddenfields'
formset[1]
< MarkForm
bound = False, valid = False, fields = (question;score;id) >
                                       formset[1].hidden_fields()
                                       [ < django.forms.boundfield.BoundField
object
at
0x10e7bdef0 >]
print(formset[1].hidden_fields())
[ < django.forms.boundfield.BoundField
object
at
0x10e7bdef0 >]
print(formset[1].hidden_fields[1])
Traceback(most
recent
call
last):
File
"<input>", line
1, in < module >
        TypeError: 'method'
object is not subscriptable
print(formset[1].hidden_fields()[1])
Traceback(most
recent
call
last):
File
"<input>", line
1, in < module >
        IndexError: list
index
out
of
range
print(formset[1].hidden_fields()[0])
< input
type = "hidden"
name = "form-1-id"
value = "148"
id = "id_form-1-id" / >
     formset[1].fields['question']
     < django.forms.models.ModelChoiceField
object
at
0x10e784780 >
print(formset[1].fields['question'])
< django.forms.models.ModelChoiceField
object
at
0x10e784780 >
form1 = formset[1]
form1.fields
OrderedDict([('question', < django.forms.models.ModelChoiceField object at 0x10e784780 >),
             ('score', < django.forms.fields.IntegerField object at 0x10e784908 >),
             ('id', < django.forms.models.ModelChoiceField object at 0x10e784550 >)])
form1.fields['question']
< django.forms.models.ModelChoiceField
object
at
0x10e784780 >
form1.fields['question']._get_choices()
< django.forms.models.ModelChoiceIterator
object
at
0x10e8b10b8 >
form1.fields['question'].label
'Question'
form1.fields['question'].value
Traceback(most
recent
call
last):
File
"<input>", line
1, in < module >
        AttributeError: 'ModelChoiceField'
object
has
no
attribute
'value'
print(formset)
< input
type = "hidden"
name = "form-TOTAL_FORMS"
value = "12"
id = "id_form-TOTAL_FORMS" / > < input
type = "hidden"
name = "form-INITIAL_FORMS"
value = "12"
id = "id_form-INITIAL_FORMS" / > < input
type = "hidden"
name = "form-MIN_NUM_FORMS"
value = "0"
id = "id_form-MIN_NUM_FORMS" / > < input
type = "hidden"
name = "form-MAX_NUM_FORMS"
value = "1000"
id = "id_form-MAX_NUM_FORMS" / >
     < tr > < th > < label
for ="id_form-0-question" > Question:< / label > < / th > < td > < select
name = "form-0-question"
id = "id_form-0-question" >
     < option
value = "" > --------- < / option >
                           < option
value = "1"
selected > 1
a < / option >
      < option
value = "2" > 1
b < / option >
      < option
value = "3" > 1
c < / option >
      < option
value = "4" > 2
a < / option >
      < option
value = "5" > 2
b < / option >
      < option
value = "6" > 2 < / option >
                    < option
value = "9" > 2 < / option >
                    < option
value = "10" > 3
a < / option >
      < option
value = "11" > 4
a < / option >
      < option
value = "12" > 7
a < / option >
      < option
value = "13" > 11
a < / option >
      < option
value = "14" > 3
a < / option >
      < / select > < / td > < / tr >
                                < tr > < th > < label
for ="id_form-0-score" > Score:< / label > < / th > < td > < input
type = "number"
name = "form-0-score"
id = "id_form-0-score" / > < input
type = "hidden"
name = "form-0-id"
value = "147"
id = "id_form-0-id" / > < / td > < / tr > < tr > < th > < label
for ="id_form-1-question" > Question:< / label > < / th > < td > < select
name = "form-1-question"
id = "id_form-1-question" >
     < option
value = "" > --------- < / option >
                           < option
value = "1" > 1
a < / option >
      < option
value = "2"
selected > 1
b < / option >
      < option
value = "3" > 1
c < / option >
      < option
value = "4" > 2
a < / option >
      < option
value = "5" > 2
b < / option >
      < option
value = "6" > 2 < / option >
                    < option
value = "9" > 2 < / option >
                    < option
value = "10" > 3
a < / option >
      < option
value = "11" > 4
a < / option >
      < option
value = "12" > 7
a < / option >
      < option
value = "13" > 11
a < / option >
      < option
value = "14" > 3
a < / option >
      < / select > < / td > < / tr >
                                < tr > < th > < label
for ="id_form-1-score" > Score:< / label > < / th > < td > < input
type = "number"
name = "form-1-score"
id = "id_form-1-score" / > < input
type = "hidden"
name = "form-1-id"
value = "148"
id = "id_form-1-id" / > < / td > < / tr > < tr > < th > < label
for ="id_form-2-question" > Question:< / label > < / th > < td > < select
name = "form-2-question"
id = "id_form-2-question" >
     < option
value = "" > --------- < / option >
                           < option
value = "1" > 1
a < / option >
      < option
value = "2" > 1
b < / option >
      < option
value = "3"
selected > 1
c < / option >
      < option
value = "4" > 2
a < / option >
      < option
value = "5" > 2
b < / option >
      < option
value = "6" > 2 < / option >
                    < option
value = "9" > 2 < / option >
                    < option
value = "10" > 3
a < / option >
      < option
value = "11" > 4
a < / option >
      < option
value = "12" > 7
a < / option >
      < option
value = "13" > 11
a < / option >
      < option
value = "14" > 3
a < / option >
      < / select > < / td > < / tr >
                                < tr > < th > < label
for ="id_form-2-score" > Score:< / label > < / th > < td > < input
type = "number"
name = "form-2-score"
id = "id_form-2-score" / > < input
type = "hidden"
name = "form-2-id"
value = "149"
id = "id_form-2-id" / > < / td > < / tr > < tr > < th > < label
for ="id_form-3-question" > Question:< / label > < / th > < td > < select
name = "form-3-question"
id = "id_form-3-question" >
     < option
value = "" > --------- < / option >
                           < option
value = "1" > 1
a < / option >
      < option
value = "2" > 1
b < / option >
      < option
value = "3" > 1
c < / option >
      < option
value = "4"
selected > 2
a < / option >
      < option
value = "5" > 2
b < / option >
      < option
value = "6" > 2 < / option >
                    < option
value = "9" > 2 < / option >
                    < option
value = "10" > 3
a < / option >
      < option
value = "11" > 4
a < / option >
      < option
value = "12" > 7
a < / option >
      < option
value = "13" > 11
a < / option >
      < option
value = "14" > 3
a < / option >
      < / select > < / td > < / tr >
                                < tr > < th > < label
for ="id_form-3-score" > Score:< / label > < / th > < td > < input
type = "number"
name = "form-3-score"
id = "id_form-3-score" / > < input
type = "hidden"
name = "form-3-id"
value = "150"
id = "id_form-3-id" / > < / td > < / tr > < tr > < th > < label
for ="id_form-4-question" > Question:< / label > < / th > < td > < select
name = "form-4-question"
id = "id_form-4-question" >
     < option
value = "" > --------- < / option >
                           < option
value = "1" > 1
a < / option >
      < option
value = "2" > 1
b < / option >
      < option
value = "3" > 1
c < / option >
      < option
value = "4" > 2
a < / option >
      < option
value = "5"
selected > 2
b < / option >
      < option
value = "6" > 2 < / option >
                    < option
value = "9" > 2 < / option >
                    < option
value = "10" > 3
a < / option >
      < option
value = "11" > 4
a < / option >
      < option
value = "12" > 7
a < / option >
      < option
value = "13" > 11
a < / option >
      < option
value = "14" > 3
a < / option >
      < / select > < / td > < / tr >
                                < tr > < th > < label
for ="id_form-4-score" > Score:< / label > < / th > < td > < input
type = "number"
name = "form-4-score"
id = "id_form-4-score" / > < input
type = "hidden"
name = "form-4-id"
value = "151"
id = "id_form-4-id" / > < / td > < / tr > < tr > < th > < label
for ="id_form-5-question" > Question:< / label > < / th > < td > < select
name = "form-5-question"
id = "id_form-5-question" >
     < option
value = "" > --------- < / option >
                           < option
value = "1" > 1
a < / option >
      < option
value = "2" > 1
b < / option >
      < option
value = "3" > 1
c < / option >
      < option
value = "4" > 2
a < / option >
      < option
value = "5" > 2
b < / option >
      < option
value = "6"
selected > 2 < / option >
                 < option
value = "9" > 2 < / option >
                    < option
value = "10" > 3
a < / option >
      < option
value = "11" > 4
a < / option >
      < option
value = "12" > 7
a < / option >
      < option
value = "13" > 11
a < / option >
      < option
value = "14" > 3
a < / option >
      < / select > < / td > < / tr >
                                < tr > < th > < label
for ="id_form-5-score" > Score:< / label > < / th > < td > < input
type = "number"
name = "form-5-score"
id = "id_form-5-score" / > < input
type = "hidden"
name = "form-5-id"
value = "152"
id = "id_form-5-id" / > < / td > < / tr > < tr > < th > < label
for ="id_form-6-question" > Question:< / label > < / th > < td > < select
name = "form-6-question"
id = "id_form-6-question" >
     < option
value = "" > --------- < / option >
                           < option
value = "1" > 1
a < / option >
      < option
value = "2" > 1
b < / option >
      < option
value = "3" > 1
c < / option >
      < option
value = "4" > 2
a < / option >
      < option
value = "5" > 2
b < / option >
      < option
value = "6" > 2 < / option >
                    < option
value = "9"
selected > 2 < / option >
                 < option
value = "10" > 3
a < / option >
      < option
value = "11" > 4
a < / option >
      < option
value = "12" > 7
a < / option >
      < option
value = "13" > 11
a < / option >
      < option
value = "14" > 3
a < / option >
      < / select > < / td > < / tr >
                                < tr > < th > < label
for ="id_form-6-score" > Score:< / label > < / th > < td > < input
type = "number"
name = "form-6-score"
id = "id_form-6-score" / > < input
type = "hidden"
name = "form-6-id"
value = "153"
id = "id_form-6-id" / > < / td > < / tr > < tr > < th > < label
for ="id_form-7-question" > Question:< / label > < / th > < td > < select
name = "form-7-question"
id = "id_form-7-question" >
     < option
value = "" > --------- < / option >
                           < option
value = "1" > 1
a < / option >
      < option
value = "2" > 1
b < / option >
      < option
value = "3" > 1
c < / option >
      < option
value = "4" > 2
a < / option >
      < option
value = "5" > 2
b < / option >
      < option
value = "6" > 2 < / option >
                    < option
value = "9" > 2 < / option >
                    < option
value = "10"
selected > 3
a < / option >
      < option
value = "11" > 4
a < / option >
      < option
value = "12" > 7
a < / option >
      < option
value = "13" > 11
a < / option >
      < option
value = "14" > 3
a < / option >
      < / select > < / td > < / tr >
                                < tr > < th > < label
for ="id_form-7-score" > Score:< / label > < / th > < td > < input
type = "number"
name = "form-7-score"
id = "id_form-7-score" / > < input
type = "hidden"
name = "form-7-id"
value = "154"
id = "id_form-7-id" / > < / td > < / tr > < tr > < th > < label
for ="id_form-8-question" > Question:< / label > < / th > < td > < select
name = "form-8-question"
id = "id_form-8-question" >
     < option
value = "" > --------- < / option >
                           < option
value = "1" > 1
a < / option >
      < option
value = "2" > 1
b < / option >
      < option
value = "3" > 1
c < / option >
      < option
value = "4" > 2
a < / option >
      < option
value = "5" > 2
b < / option >
      < option
value = "6" > 2 < / option >
                    < option
value = "9" > 2 < / option >
                    < option
value = "10" > 3
a < / option >
      < option
value = "11"
selected > 4
a < / option >
      < option
value = "12" > 7
a < / option >
      < option
value = "13" > 11
a < / option >
      < option
value = "14" > 3
a < / option >
      < / select > < / td > < / tr >
                                < tr > < th > < label
for ="id_form-8-score" > Score:< / label > < / th > < td > < input
type = "number"
name = "form-8-score"
id = "id_form-8-score" / > < input
type = "hidden"
name = "form-8-id"
value = "155"
id = "id_form-8-id" / > < / td > < / tr > < tr > < th > < label
for ="id_form-9-question" > Question:< / label > < / th > < td > < select
name = "form-9-question"
id = "id_form-9-question" >
     < option
value = "" > --------- < / option >
                           < option
value = "1" > 1
a < / option >
      < option
value = "2" > 1
b < / option >
      < option
value = "3" > 1
c < / option >
      < option
value = "4" > 2
a < / option >
      < option
value = "5" > 2
b < / option >
      < option
value = "6" > 2 < / option >
                    < option
value = "9" > 2 < / option >
                    < option
value = "10" > 3
a < / option >
      < option
value = "11" > 4
a < / option >
      < option
value = "12"
selected > 7
a < / option >
      < option
value = "13" > 11
a < / option >
      < option
value = "14" > 3
a < / option >
      < / select > < / td > < / tr >
                                < tr > < th > < label
for ="id_form-9-score" > Score:< / label > < / th > < td > < input
type = "number"
name = "form-9-score"
id = "id_form-9-score" / > < input
type = "hidden"
name = "form-9-id"
value = "156"
id = "id_form-9-id" / > < / td > < / tr > < tr > < th > < label
for ="id_form-10-question" > Question:< / label > < / th > < td > < select
name = "form-10-question"
id = "id_form-10-question" >
     < option
value = "" > --------- < / option >
                           < option
value = "1" > 1
a < / option >
      < option
value = "2" > 1
b < / option >
      < option
value = "3" > 1
c < / option >
      < option
value = "4" > 2
a < / option >
      < option
value = "5" > 2
b < / option >
      < option
value = "6" > 2 < / option >
                    < option
value = "9" > 2 < / option >
                    < option
value = "10" > 3
a < / option >
      < option
value = "11" > 4
a < / option >
      < option
value = "12" > 7
a < / option >
      < option
value = "13"
selected > 11
a < / option >
      < option
value = "14" > 3
a < / option >
      < / select > < / td > < / tr >
                                < tr > < th > < label
for ="id_form-10-score" > Score:< / label > < / th > < td > < input
type = "number"
name = "form-10-score"
id = "id_form-10-score" / > < input
type = "hidden"
name = "form-10-id"
value = "157"
id = "id_form-10-id" / > < / td > < / tr > < tr > < th > < label
for ="id_form-11-question" > Question:< / label > < / th > < td > < select
name = "form-11-question"
id = "id_form-11-question" >
     < option
value = "" > --------- < / option >
                           < option
value = "1" > 1
a < / option >
      < option
value = "2" > 1
b < / option >
      < option
value = "3" > 1
c < / option >
      < option
value = "4" > 2
a < / option >
      < option
value = "5" > 2
b < / option >
      < option
value = "6" > 2 < / option >
                    < option
value = "9" > 2 < / option >
                    < option
value = "10" > 3
a < / option >
      < option
value = "11" > 4
a < / option >
      < option
value = "12" > 7
a < / option >
      < option
value = "13" > 11
a < / option >
      < option
value = "14"
selected > 3
a < / option >
      < / select > < / td > < / tr >
                                < tr > < th > < label
for ="id_form-11-score" > Score:< / label > < / th > < td > < input
type = "number"
name = "form-11-score"
id = "id_form-11-score" / > < input
type = "hidden"
name = "form-11-id"
value = "158"
id = "id_form-11-id" / > < / td > < / tr >
                                      form1.fields['question'].initial
form1.fields['question'].widget
< django.forms.widgets.Select
object
at
0x10e7847b8 >
formset[4].fields['question'].widget
< django.forms.widgets.Select
object
at
0x10e78d748 >
formset[4].fields['question']
< django.forms.models.ModelChoiceField
object
at
0x10e78d710 >
formset[4].fields['score']
< django.forms.fields.IntegerField
object
at
0x10e78d940 >
formset[4].fields['score'].clean()
Traceback(most
recent
call
last):
File
"<input>", line
1, in < module >
        TypeError: clean()
missing
1
required
positional
argument: 'value'
formset[4].fields['score'].value
Traceback(most
recent
call
last):
File
"<input>", line
1, in < module >
        AttributeError: 'IntegerField'
object
has
no
attribute
'value'
formset[4].fields['score'].help_text
''
formset[4].fields['score']
< django.forms.fields.IntegerField
object
at
0x10e78d940 >
formset[4].fields['score'] = 4
formset[4].fields['score']
4
formset[1].fields['score']
< django.forms.fields.IntegerField
object
at
0x10e784908 >
formset[2].fields['score']
< django.forms.fields.IntegerField
object
at
0x10e784a58 >
formset[2]
< MarkForm
bound = False, valid = False, fields = (question;score;id) >
                                       print(formset[2])
                                       < tr > < th > < label
for ="id_form-2-question" > Question:< / label > < / th > < td > < select
name = "form-2-question"
id = "id_form-2-question" >
     < option
value = "" > --------- < / option >
                           < option
value = "1" > 1
a < / option >
      < option
value = "2" > 1
b < / option >
      < option
value = "3"
selected > 1
c < / option >
      < option
value = "4" > 2
a < / option >
      < option
value = "5" > 2
b < / option >
      < option
value = "6" > 2 < / option >
                    < option
value = "9" > 2 < / option >
                    < option
value = "10" > 3
a < / option >
      < option
value = "11" > 4
a < / option >
      < option
value = "12" > 7
a < / option >
      < option
value = "13" > 11
a < / option >
      < option
value = "14" > 3
a < / option >
      < / select > < / td > < / tr >
                                < tr > < th > < label
for ="id_form-2-score" > Score:< / label > < / th > < td > < input
type = "number"
name = "form-2-score"
id = "id_form-2-score" / > < input
type = "hidden"
name = "form-2-id"
value = "149"
id = "id_form-2-id" / > < / td > < / tr >
                                     print(formset[2].fields)
OrderedDict([('question', < django.forms.models.ModelChoiceField object at 0x10e784828 >),
             ('score', < django.forms.fields.IntegerField object at 0x10e784a58 >),
             ('id', < django.forms.models.ModelChoiceField object at 0x10e784d68 >)])
print(formset[2].visible_fields())
[ < django.forms.boundfield.BoundField
object
at
0x10e7bdf60 >, < django.forms.boundfield.BoundField
object
at
0x10e7ac400 >]
print(formset[2].visible_fields()[1])
< input
type = "number"
name = "form-2-score"
id = "id_form-2-score" / >
     print(formset[2].visible_fields()[0])
     < select
name = "form-2-question"
id = "id_form-2-question" >
     < option
value = "" > --------- < / option >
                           < option
value = "1" > 1
a < / option >
      < option
value = "2" > 1
b < / option >
      < option
value = "3"
selected > 1
c < / option >
      < option
value = "4" > 2
a < / option >
      < option
value = "5" > 2
b < / option >
      < option
value = "6" > 2 < / option >
                    < option
value = "9" > 2 < / option >
                    < option
value = "10" > 3
a < / option >
      < option
value = "11" > 4
a < / option >
      < option
value = "12" > 7
a < / option >
      < option
value = "13" > 11
a < / option >
      < option
value = "14" > 3
a < / option >
      < / select >
          print(formset[2].fields[0])
Traceback(most
recent
call
last):
File
"<input>", line
1, in < module >
        KeyError: 0
print(formset[2].fields['question'])
< django.forms.models.ModelChoiceField
object
at
0x10e784828 >
print(formset[2].visible_fields()[0])
< select
name = "form-2-question"
id = "id_form-2-question" >
     < option
value = "" > --------- < / option >
                           < option
value = "1" > 1
a < / option >
      < option
value = "2" > 1
b < / option >
      < option
value = "3"
selected > 1
c < / option >
      < option
value = "4" > 2
a < / option >
      < option
value = "5" > 2
b < / option >
      < option
value = "6" > 2 < / option >
                    < option
value = "9" > 2 < / option >
                    < option
value = "10" > 3
a < / option >
      < option
value = "11" > 4
a < / option >
      < option
value = "12" > 7
a < / option >
      < option
value = "13" > 11
a < / option >
      < option
value = "14" > 3
a < / option >
      < / select >
          formset[2].question
Traceback(most
recent
call
last):
File
"<input>", line
1, in < module >
        AttributeError: 'MarkForm'
object
has
no
attribute
'question'
formset[2].score
Traceback(most
recent
call
last):
File
"<input>", line
1, in < module >
        AttributeError: 'MarkForm'
object
has
no
attribute
'score'
formset[2].visible_fields.score
Traceback(most
recent
call
last):
File
"<input>", line
1, in < module >
        AttributeError: 'function'
object
has
no
attribute
'score'
formset[2].visible_fields[0]
Traceback(most
recent
call
last):
File
"<input>", line
1, in < module >
        TypeError: 'method'
object is not subscriptable
formset[2].visible_fields()[0]
< django.forms.boundfield.BoundField
object
at
0x10e7bdf60 >
formset[2].visible_fields()[0].question
Traceback(most
recent
call
last):
File
"<input>", line
1, in < module >
        AttributeError: 'BoundField'
object
has
no
attribute
'question'
form1.question
Traceback(most
recent
call
last):
File
"<input>", line
1, in < module >
        AttributeError: 'MarkForm'
object
has
no
attribute
'question'
form1.score
Traceback(most
recent
call
last):
File
"<input>", line
1, in < module >
        AttributeError: 'MarkForm'
object
has
no
attribute
'score'
form1.fields
OrderedDict([('question', < django.forms.models.ModelChoiceField object at 0x10e784780 >),
             ('score', < django.forms.fields.IntegerField object at 0x10e784908 >),
             ('id', < django.forms.models.ModelChoiceField object at 0x10e784550 >)])
form1['question']
< django.forms.boundfield.BoundField
object
at
0x10e7bdf28 >
form1['question'].name
'question'
form1['question'].as_text()
'<input type="text" name="form-1-question" value="2" id="id_form-1-question" />'
for formpart in form1:
    formpart.as_text()
for formpart in form1:
    print(formpart.as_text())

    < input
type = "text"
name = "form-1-question"
value = "2"
id = "id_form-1-question" / >
     < input
type = "text"
name = "form-1-score"
id = "id_form-1-score" / >
     < input
type = "text"
name = "form-1-id"
value = "148"
id = "id_form-1-id" / >
for formpart in form1:
    print(formpart)

    < select
name = "form-1-question"
id = "id_form-1-question" >
     < option
value = "" > --------- < / option >
                           < option
value = "1" > 1
a < / option >
      < option
value = "2"
selected > 1
b < / option >
      < option
value = "3" > 1
c < / option >
      < option
value = "4" > 2
a < / option >
      < option
value = "5" > 2
b < / option >
      < option
value = "6" > 2 < / option >
                    < option
value = "9" > 2 < / option >
                    < option
value = "10" > 3
a < / option >
      < option
value = "11" > 4
a < / option >
      < option
value = "12" > 7
a < / option >
      < option
value = "13" > 11
a < / option >
      < option
value = "14" > 3
a < / option >
      < / select >
          < input
type = "number"
name = "form-1-score"
id = "id_form-1-score" / >
     < input
type = "hidden"
name = "form-1-id"
value = "148"
id = "id_form-1-id" / >
     students = Student.objects.filter(classgroups__in=sitting.classgroup).order_by(pk).order_by(User.last_name)
Traceback(most
recent
call
last):
File
"<input>", line
1, in < module >
        File
"/Users/wright.j/django-test/lib/python3.6/site-packages/django/db/models/manager.py", line
82, in manager_method
return getattr(self.get_queryset(), name)(*args, **kwargs)
File
"/Users/wright.j/django-test/lib/python3.6/site-packages/django/db/models/query.py", line
836, in filter
return self._filter_or_exclude(False, *args, **kwargs)
File
"/Users/wright.j/django-test/lib/python3.6/site-packages/django/db/models/query.py", line
854, in _filter_or_exclude
clone.query.add_q(Q(*args, **kwargs))
File
"/Users/wright.j/django-test/lib/python3.6/site-packages/django/db/models/sql/query.py", line
1253, in add_q
clause, _ = self._add_q(q_object, self.used_aliases)
File
"/Users/wright.j/django-test/lib/python3.6/site-packages/django/db/models/sql/query.py", line
1277, in _add_q
split_subq = split_subq,
File
"/Users/wright.j/django-test/lib/python3.6/site-packages/django/db/models/sql/query.py", line
1215, in build_filter
condition = self.build_lookup(lookups, col, value)
File
"/Users/wright.j/django-test/lib/python3.6/site-packages/django/db/models/sql/query.py", line
1085, in build_lookup
lookup = lookup_class(lhs, rhs)
File
"/Users/wright.j/django-test/lib/python3.6/site-packages/django/db/models/lookups.py", line
18, in __init__
self.rhs = self.get_prep_lookup()
File
"/Users/wright.j/django-test/lib/python3.6/site-packages/django/db/models/fields/related_lookups.py", line
50, in get_prep_lookup
self.rhs = [get_normalized_value(val, self.lhs)[0] for val in self.rhs]
TypeError: 'ClassGroup'
object is not iterable
students = Student.objects.filter(classgroups=sitting.classgroup).order_by(pk).order_by(User.last_name)
Traceback(most
recent
call
last):
File
"<input>", line
1, in < module >
NameError: name
'pk' is not defined
students = Student.objects.filter(classgroups=sitting.classgroup).order_by('pk').order_by('user.last_name')
scores = {}
for student in students:
    total = Mark.objects.filter(sitting=sitting).filter(student=student).aggregate(Sum('score'))
    scores[student] = total
File
"<input>", line
2
for student in students:
    ^
    IndentationError: unexpected
    indent
    scores = {}
    for student in students:
        total = Mark.objects.filter(sitting=sitting).filter(student=student).aggregate(Sum('score'))
        scores[student] = total
    Traceback(most
    recent
    call
    last):
    File
    "/Users/wright.j/django-test/lib/python3.6/site-packages/django/db/backends/utils.py", line
    85, in _execute
    return self.cursor.execute(sql, params)
    File
    "/Users/wright.j/django-test/lib/python3.6/site-packages/django/db/backends/sqlite3/base.py", line
    303, in execute
    return Database.Cursor.execute(self, query, params)
    sqlite3.OperationalError: no
    such
    column: user.last_name
    The
    above
    exception
    was
    the
    direct
    cause
    of
    the
    following
    exception:
    Traceback(most
    recent
    call
    last):
    File
    "<input>", line
    2, in < module >
    File
    "/Users/wright.j/django-test/lib/python3.6/site-packages/django/db/models/query.py", line
    272, in __iter__
    self._fetch_all()
    File
    "/Users/wright.j/django-test/lib/python3.6/site-packages/django/db/models/query.py", line
    1179, in _fetch_all
    self._result_cache = list(self._iterable_class(self))
    File
    "/Users/wright.j/django-test/lib/python3.6/site-packages/django/db/models/query.py", line
    54, in __iter__
    results = compiler.execute_sql(chunked_fetch=self.chunked_fetch, chunk_size=self.chunk_size)
    File
    "/Users/wright.j/django-test/lib/python3.6/site-packages/django/db/models/sql/compiler.py", line
    1064, in execute_sql
    cursor.execute(sql, params)
    File
    "/Users/wright.j/django-test/lib/python3.6/site-packages/django/db/backends/utils.py", line
    100, in execute
    return super().execute(sql, params)
    File
    "/Users/wright.j/django-test/lib/python3.6/site-packages/django/db/backends/utils.py", line
    68, in execute
    return self._execute_with_wrappers(sql, params, many=False, executor=self._execute)
    File
    "/Users/wright.j/django-test/lib/python3.6/site-packages/django/db/backends/utils.py", line
    77, in _execute_with_wrappers
    return executor(sql, params, many, context)
    File
    "/Users/wright.j/django-test/lib/python3.6/site-packages/django/db/backends/utils.py", line
    85, in _execute
    return self.cursor.execute(sql, params)
    File
    "/Users/wright.j/django-test/lib/python3.6/site-packages/django/db/utils.py", line
    89, in __exit__
    raise dj_exc_value.with_traceback(traceback) from exc_value
    File
    "/Users/wright.j/django-test/lib/python3.6/site-packages/django/db/backends/utils.py", line
    85, in _execute
    return self.cursor.execute(sql, params)
    File
    "/Users/wright.j/django-test/lib/python3.6/site-packages/django/db/backends/sqlite3/base.py", line
    303, in execute
    return Database.Cursor.execute(self, query, params)
    django.db.utils.OperationalError: no
    such
    column: user.last_name
    students = Student.objects.filter(classgroups=sitting.classgroup).order_by('pk').order_by('User.last_name')
    scores = {}
    for student in students:
        total = Mark.objects.filter(sitting=sitting).filter(student=student).aggregate(Sum('score'))
        scores[student] = total
    Traceback(most
    recent
    call
    last):
    File
    "/Users/wright.j/django-test/lib/python3.6/site-packages/django/db/backends/utils.py", line
    85, in _execute
    return self.cursor.execute(sql, params)
    File
    "/Users/wright.j/django-test/lib/python3.6/site-packages/django/db/backends/sqlite3/base.py", line
    303, in execute
    return Database.Cursor.execute(self, query, params)
    sqlite3.OperationalError: no
    such
    column: User.last_name
    The
    above
    exception
    was
    the
    direct
    cause
    of
    the
    following
    exception:
    Traceback(most
    recent
    call
    last):
    File
    "<input>", line
    2, in < module >
    File
    "/Users/wright.j/django-test/lib/python3.6/site-packages/django/db/models/query.py", line
    272, in __iter__
    self._fetch_all()
    File
    "/Users/wright.j/django-test/lib/python3.6/site-packages/django/db/models/query.py", line
    1179, in _fetch_all
    self._result_cache = list(self._iterable_class(self))
    File
    "/Users/wright.j/django-test/lib/python3.6/site-packages/django/db/models/query.py", line
    54, in __iter__
    results = compiler.execute_sql(chunked_fetch=self.chunked_fetch, chunk_size=self.chunk_size)
    File
    "/Users/wright.j/django-test/lib/python3.6/site-packages/django/db/models/sql/compiler.py", line
    1064, in execute_sql
    cursor.execute(sql, params)
    File
    "/Users/wright.j/django-test/lib/python3.6/site-packages/django/db/backends/utils.py", line
    100, in execute
    return super().execute(sql, params)
    File
    "/Users/wright.j/django-test/lib/python3.6/site-packages/django/db/backends/utils.py", line
    68, in execute
    return self._execute_with_wrappers(sql, params, many=False, executor=self._execute)
    File
    "/Users/wright.j/django-test/lib/python3.6/site-packages/django/db/backends/utils.py", line
    77, in _execute_with_wrappers
    return executor(sql, params, many, context)
    File
    "/Users/wright.j/django-test/lib/python3.6/site-packages/django/db/backends/utils.py", line
    85, in _execute
    return self.cursor.execute(sql, params)
    File
    "/Users/wright.j/django-test/lib/python3.6/site-packages/django/db/utils.py", line
    89, in __exit__
    raise dj_exc_value.with_traceback(traceback) from exc_value
    File
    "/Users/wright.j/django-test/lib/python3.6/site-packages/django/db/backends/utils.py", line
    85, in _execute
    return self.cursor.execute(sql, params)
    File
    "/Users/wright.j/django-test/lib/python3.6/site-packages/django/db/backends/sqlite3/base.py", line
    303, in execute
    return Database.Cursor.execute(self, query, params)
    django.db.utils.OperationalError: no
    such
    column: User.last_name
    students = Student.objects.filter(classgroups=sitting.classgroup).order_by('pk').order_by('__user__last_name')
    scores = {}
    for student in students:
        total = Mark.objects.filter(sitting=sitting).filter(student=student).aggregate(Sum('score'))
        scores[student] = total
    Traceback(most
    recent
    call
    last):
    File
    "<input>", line
    2, in < module >
    File
    "/Users/wright.j/django-test/lib/python3.6/site-packages/django/db/models/query.py", line
    272, in __iter__
    self._fetch_all()
    File
    "/Users/wright.j/django-test/lib/python3.6/site-packages/django/db/models/query.py", line
    1179, in _fetch_all
    self._result_cache = list(self._iterable_class(self))
    File
    "/Users/wright.j/django-test/lib/python3.6/site-packages/django/db/models/query.py", line
    54, in __iter__
    results = compiler.execute_sql(chunked_fetch=self.chunked_fetch, chunk_size=self.chunk_size)
    File
    "/Users/wright.j/django-test/lib/python3.6/site-packages/django/db/models/sql/compiler.py", line
    1051, in execute_sql
    sql, params = self.as_sql()
    File
    "/Users/wright.j/django-test/lib/python3.6/site-packages/django/db/models/sql/compiler.py", line
    446, in as_sql
    extra_select, order_by, group_by = self.pre_sql_setup()
    File
    "/Users/wright.j/django-test/lib/python3.6/site-packages/django/db/models/sql/compiler.py", line
    51, in pre_sql_setup
    order_by = self.get_order_by()
    File
    "/Users/wright.j/django-test/lib/python3.6/site-packages/django/db/models/sql/compiler.py", line
    316, in get_order_by
    field, self.query.get_meta(), default_order = asc))
    File
    "/Users/wright.j/django-test/lib/python3.6/site-packages/django/db/models/sql/compiler.py", line
    661, in find_ordering_name
    field, targets, alias, joins, path, opts = self._setup_joins(pieces, opts, alias)
    File
    "/Users/wright.j/django-test/lib/python3.6/site-packages/django/db/models/sql/compiler.py", line
    694, in _setup_joins
    pieces, opts, alias)
    File
    "/Users/wright.j/django-test/lib/python3.6/site-packages/django/db/models/sql/query.py", line
    1448, in setup_joins
    names, opts, allow_many, fail_on_missing = True)
    File
    "/Users/wright.j/django-test/lib/python3.6/site-packages/django/db/models/sql/query.py", line
    1379, in names_to_path
    "Choices are: %s" % (name, ", ".join(available)))
    django.core.exceptions.FieldError: Cannot
    resolve
    keyword
    ''
    into
    field.Choices
    are: Gender, classgroups, id, idnumber, mark, tutorgroup, tutorgroup_id, user, user_id, year
    students = Student.objects.filter(classgroups=sitting.classgroup).order_by('pk').order_by('user__last_name')
    scores = {}
    for student in students:
        total = Mark.objects.filter(sitting=sitting).filter(student=student).aggregate(Sum('score'))
    scores[student] = total
    Traceback(most
    recent
    call
    last):
    File
    "<input>", line
    3, in < module >
            NameError: name
    'Sum' is not defined
    from django.db.models import Sum

    scores = {}
    for student in students:
        total = Mark.objects.filter(sitting=sitting).filter(student=student).aggregate(Sum('score'))
    scores[student] = total
    scores
    { < Student: BUKHARY
    Ameera >: {'score__sum': None}, < Student: JAIN
    Arshi >: {'score__sum': None}, < Student: IVEC
    Brycen >: {'score__sum': None}, < Student: TAN
    Daryl >: {'score__sum': 12}, < Student: CHIN
    Gail >: {'score__sum': None}, < Student: BROWN
    Gary >: {'score__sum': None}, < Student: TUNKU
    HAMMAM
    Harris >: {'score__sum': None}, < Student: ONG
    Jeng
    Ian >: {'score__sum': None}, < Student: KAGALINGAN
    Jhensen >: {'score__sum': None}, < Student: SIMANDJOENTAK
    Lance >: {'score__sum': None}, < Student: JAMIESON
    Maia >: {'score__sum': None}, < Student: AAMANN
    Marie >: {'score__sum': None}, < Student: POWELL
    Natasha >: {'score__sum': None}, < Student: TIRATHRAI
    Neel >: {'score__sum': None}, < Student: CHUNG
    Nixon >: {'score__sum': None}, < Student: DIWASASRI
    Radhita >: {'score__sum': None}, < Student: ITO
    Rafael >: {'score__sum': None}, < Student: VERKHEDKAR
    Vira >: {'score__sum': None}}
    for score in scores:
        print(score)
    BUKHARY
    Ameera
    JAIN
    Arshi
    IVEC
    Brycen
    TAN
    Daryl
    CHIN
    Gail
    BROWN
    Gary
    TUNKU
    HAMMAM
    Harris
    ONG
    Jeng
    Ian
    KAGALINGAN
    Jhensen
    SIMANDJOENTAK
    Lance
    JAMIESON
    Maia
    AAMANN
    Marie
    POWELL
    Natasha
    TIRATHRAI
    Neel
    CHUNG
    Nixon
    DIWASASRI
    Radhita
    ITO
    Rafael
    VERKHEDKAR
    Vira
    totals = Mark.objects.filter(sitting=sitting).filter(student=student).aggregate(Sum('score'))
    totals
    {'score__sum': None}
    scores[1]
    Traceback(most
    recent
    call
    last):
    File
    "<input>", line
    1, in < module >
            KeyError: 1
    scores[student]
    {'score__sum': None}
    scores[student]['score__sum']
    daryl = Student.objects.get(user__last_name='Tan')
    Traceback(most
    recent
    call
    last):
    File
    "<input>", line
    1, in < module >
            File
    "/Users/wright.j/django-test/lib/python3.6/site-packages/django/db/models/manager.py", line
    82, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
    File
    "/Users/wright.j/django-test/lib/python3.6/site-packages/django/db/models/query.py", line
    403, in get
    self.model._meta.object_name
    school.models.DoesNotExist: Student
    matching
    query
    does
    not exist.
    daryl = Student.objects.get(user__last_name='Tann')
    Traceback(most
    recent
    call
    last):
    File
    "<input>", line
    1, in < module >
    File
    "/Users/wright.j/django-test/lib/python3.6/site-packages/django/db/models/manager.py", line
    82, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
    File
    "/Users/wright.j/django-test/lib/python3.6/site-packages/django/db/models/query.py", line
    403, in get
    self.model._meta.object_name
    school.models.DoesNotExist: Student
    matching
    query
    does
    not exist.
    daryl = Student.objects.get(user__last_name='TAN')
    Traceback(most
    recent
    call
    last):
    File
    "<input>", line
    1, in < module >
    File
    "/Users/wright.j/django-test/lib/python3.6/site-packages/django/db/models/manager.py", line
    82, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
    File
    "/Users/wright.j/django-test/lib/python3.6/site-packages/django/db/models/query.py", line
    403, in get
    self.model._meta.object_name
    school.models.DoesNotExist: Student
    matching
    query
    does
    not exist.
    daryl = Student.objects.get(user__last_name='TAN ')
    Traceback(most
    recent
    call
    last):
    File
    "<input>", line
    1, in < module >
    File
    "/Users/wright.j/django-test/lib/python3.6/site-packages/django/db/models/manager.py", line
    82, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
    File
    "/Users/wright.j/django-test/lib/python3.6/site-packages/django/db/models/query.py", line
    403, in get
    self.model._meta.object_name
    school.models.DoesNotExist: Student
    matching
    query
    does
    not exist.
    daryl = Student.objects.get(pk=34)
    daryl
    < Student: POWELL
    Natasha >
    daryl = Student.objects.get(pk=32)
    daryl
    < Student: KAGALINGAN
    Jhensen >
    daryl = Student.objects.get(pk=31)
    daryl
    < Student: JAMIESON
    Maia >
    daryl = Student.objects.get(pk=36)
    daryl
    < Student: TAN
    Daryl >
    scores[daryl]
    {'score__sum': 12}
    scores[daryl]['score__sum']
    12
    for score in scores[daryl]:
        print(score)
    score__sum
    for score in scores[daryl]:
        print(score['score__sum'])
    Traceback(most
    recent
    call
    last):
    File
    "<input>", line
    2, in < module >
    TypeError: string
    indices
    must
    be
    integers
    for score in scores[daryl]:
        print(score[0])
    s
