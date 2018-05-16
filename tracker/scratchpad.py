MarkFormet = modelformset_factory(Mark, fields=('score',))
formset = MarkFormSet(queryset=marks)
marks = Mark.objects.filter(sitting=sitting).order_by('question__qorder').order_by('student')


formset = MarkFormSet(queryset=Mark.objects.filter(sitting=sitting).order_by('question__qorder').order_by('student'))