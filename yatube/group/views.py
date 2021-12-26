from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def group_posts(request):
    return HttpResponse('This is the page where you would see groups posts.')
