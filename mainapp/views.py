from django.shortcuts import render
from django.http import HttpResponse
def firstViews(response):
    return HttpResponse('<h1>hi from views from mainApp</h1')


# Create your views here.
