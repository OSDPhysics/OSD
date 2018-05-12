from django.core.exceptions import PermissionDenied
from school.models import Student, Teacher
from django.contrib.auth.models import User


def teacher_only(function):
    def wrap(request, *args, **kwargs):

        if request.user.groups.filter(name='Teachers').exists():
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied

    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap


def admin_only(function):
    def wrap(request, *args, **kwargs):

        if request.user.groups.filter(name='Administrators').exists():
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied

    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap


def teacher_or_own_only(function):
    """display only if viewing student's own work or if requesting user is a teacher"""

    def wrap(request, *args, **kwargs):

        if request.user.groups.filter(name='Teachers').exists():
            return function(request, *args, **kwargs)

        # TODO: this is broken!
        requested_student = Student.objects.get(pk=kwargs['pk'])
        if request.user.pk == requested_student:
            return function(request, *args, **kwargs)

        else:
            raise PermissionDenied

    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap


def teacer_or_lm_only(function):
    """ restrict viewing to the requesting (teacher) user or their line managers only"""

    def wrap(request, *args, **kwargs):
        requested_teacher = Teacher.objects.get(pk=kwargs['teacher_pk'])
        requesting_user = request.user # Remember that LMs are defined by a foreign key to a USER, not TEACHER.
        if requested_teacher.user == requesting_user:
            return function(request, *args, **kwargs)

        linemanagers= [requested_teacher]
        current_teacher = requested_teacher
        while True:

            if current_teacher.line_manager:
                linemanagers.append(current_teacher.line_manager)
                if requesting_user in linemanagers:
                    return function(request, *args, **kwargs)
                else:
                    current_teacher = current_teacher.line_manager
            else:
                raise PermissionDenied

        else:
            raise PermissionDenied
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap
