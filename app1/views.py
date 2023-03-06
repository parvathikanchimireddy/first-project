from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def hari(request):
    return HttpResponse('<h1>Hari is very briliant boy in the class<h1>')
def amma(request):
    return HttpResponse('<marquee><h2>I Love You Amma</h2></marquee>')
