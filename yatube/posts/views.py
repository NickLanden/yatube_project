from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse('This is the initial page of the site. I am pleased you have visited me!')
