from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    return HttpResponse("Welcome to Day2 coding of Django.")

def about(request):
    return render(request, 'generator_day2/about.html')

def password(request):
    return render(request, 'generator_day2/pwd.html')

def passwordgen(request):

    characters = list('abcdefghijklmnopqrstuvwxyz')   
    
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWSYZ'))
    
    if request.GET.get('special'):
        characters.extend(list('!@#$^&*()_+'))

    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    length = int(request.GET.get('length'))
    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characters)

    return render(request, 'generator_day2/pwdgenerated.html', {'password': thepassword})

