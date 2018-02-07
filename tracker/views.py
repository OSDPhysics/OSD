from django.shortcuts import render

# Create your views here.
def front_login(request):
    return render(request, 'tracker/front_login.html', {})  