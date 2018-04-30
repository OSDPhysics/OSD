from django.shortcuts import render

# Create your views here.

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import *
import logging
from .functions.adddata import *
import os

logger = logging.getLogger(__name__)


@login_required
def home(request):

    return render(request, 'teachnet/home.html')
