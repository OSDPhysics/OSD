# Create your views here.

from django.shortcuts import render, get_object_or_404, HttpResponseRedirect

from osd.decorators import teacher_only, teacer_or_lm_only
from school.models import Teacher
from teachnet.models import Skill, Objective
from teachnet.forms import ObjectiveForm


def can_view_full_profile(requester, user):
    if requester.pk == user.pk: # viewing own profile
        return True

    # check if the requester is the line manager of the user
    islinemanager = Teacher.objects.filter(line_manager=requester).count()

    if islinemanager >= 1:
        return True

    # We're not the user, or the line manager, so kick them out
    return False

@teacher_only
def home(request):

    return render(request, 'teachnet/home.html')

@teacher_only
def teacherskills(request):
    teachers = Teacher.objects.all()
    skill = 'All'
    return render(request, 'teachnet/teacher_skills.html', {'teachers': teachers,
                                                            'skill': skill})


@teacher_only
def profile(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)

    if can_view_full_profile(request.user, teacher):
        teacher_objectives = Objective.objects.filter(teacher=teacher).order_by('date_created').order_by('date_approved')
        return render(request, 'teachnet/full_profile.html', {'teacher': teacher,
                                                              'teacher_objectives': teacher_objectives})

    else:
        return render(request, 'teachnet/forbidden.html') # TODO: change to a limited profile


@teacher_only
def teacherwithskill(request, pk):
    teachers = Teacher.objects.filter(skills__pk=pk)
    skill = Skill.objects.get(pk=pk)
    return render(request, 'teachnet/teacher_skills.html', {'teachers': teachers,
                                                            'skill': skill})

@teacher_only
def objectives(request,pk):
    teacher = get_object_or_404(Teacher, pk=pk)

    if can_view_full_profile(request.user, teacher):
        return render(request, 'teachnet/objectives.html', {'teacher': teacher})

    else:
        return render(request, 'teachnet/forbidden.html')


@teacer_or_lm_only
def set_objectives(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ObjectiveForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('../'+str(pk))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ObjectiveForm()

    return render(request, 'teachnet/update_objective.html', {'form': form})

