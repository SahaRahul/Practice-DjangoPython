from django.shortcuts import render 
# from django.http import HttpResponse
from .models import Project

# Create your views here.
def home(request):
    projects = Project.objects.all()
    # return HttpResponse("Our new home page.")
    return render(request, 'personal_prof_app/home.html', {'projects':projects})