from django.shortcuts import render
from django.http import HttpResponse

#Blog Page View
def blog(request):
    return HttpResponse('Blog Page')


