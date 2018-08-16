# Create your views here.

from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.urls import reverse

from osd.decorators import teacher_only, teacer_or_lm_only
from school.models import Teacher
from teachnet.models import Skill, Objective
from teachnet.forms import ObjectiveForm


def can_view_full_profile(requester, user):
    if requester.pk == user.pk:  # viewing own profile
        return True

    # check if the requester is the line manager of the user
    # TODO: This currently is 1 for ANY line manager! Must fix so ONLY the LM for the teacher
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
def profile(request, teacher_pk):
    teacher = get_object_or_404(Teacher, pk=teacher_pk)

    if can_view_full_profile(request.user, teacher):
        teacher_objectives = Objective.objects.filter(teacher=teacher).order_by('date_created').order_by(
            'date_approved')
        return render(request, 'teachnet/full_profile.html', {'teacher': teacher,
                                                              'teacher_objectives': teacher_objectives})

    else:
        return render(request, 'teachnet/forbidden.html')  # TODO: change to a limited profile


@teacher_only
def teacherwithskill(request, pk):
    teachers = Teacher.objects.filter(skills__pk=pk)
    skill = Skill.objects.get(pk=pk)
    return render(request, 'teachnet/teacher_skills.html', {'teachers': teachers,
                                                            'skill': skill})


@teacher_only
def objectives(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)

    if can_view_full_profile(request.user, teacher):
        return render(request, 'teachnet/objectives.html', {'teacher': teacher})

    else:
        return render(request, 'teachnet/forbidden.html')


@teacer_or_lm_only
def new_objectives(request, teacher_pk):
    teacher = get_object_or_404(Teacher, pk=teacher_pk)

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ObjectiveForm(request.POST)
        # check whdiether it's valid:
        if form.is_valid():
            newobjective = form.save(commit=False)  # needed so we can now modify the form data
            newobjective.teacher = teacher  # Set teacher to be saved

            form.save()
            return HttpResponseRedirect(reverse('profile', args=(teacher.pk,)))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ObjectiveForm()

    return render(request, 'teachnet/new_objective.html', {'form': form})


@teacer_or_lm_only
def edit_objective(request, teacher_pk, objective_pk):
    teacher = get_object_or_404(Teacher, pk=teacher_pk)
    objective = get_object_or_404(Objective, pk=objective_pk)

    if request.method == 'POST':
        form = ObjectiveForm(request.POST, instance=objective)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('profile', args=(teacher.pk,)))

    else:
        form = ObjectiveForm(instance=objective)

    return render(request, 'teachnet/edit_objective.html', {'form': form},
                  {'objective': objective})
