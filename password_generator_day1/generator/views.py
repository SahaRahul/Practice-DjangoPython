from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home1(request):
    return HttpResponse("Hello there friend.")

def home2(request):
    return render(request, 'generator/home.html')

def home(request):
    # Pretty cool to pass the value into the Web page programmatically
    return render(request, 'generator/home3.html', {'password': 'fdfe#324d'})

def letsDance(request):
    return HttpResponse('<h1> We are dancing. </h1>')