from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

# Create your views here.
def splash(request):
    return render(request, 'tracker/splash.html', {})

#def signup(request):
#    return render(request, 'tracker/signup.html', {})

def login(request):
    return render(request, 'tracker/login.html', {})

def teachers(request):
    return render(request, 'tracker/teachers.html', {})

def students(request):
    return render(request, 'tracker/students.html', {})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('')
    else:
        form = UserCreationForm()
    return render(request, 'tracker/signup.html', {'form': form})