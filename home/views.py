from django.shortcuts import render
from django.http import HttpResponse

#Home Page View
def home(request):
    return render(request, 'home.html')

#About Page View
def about(request):
    return render(request, 'about.html')

#Resume Page View
def resume(request):
    return render(request, 'resume.html')

#Portfolio Page View
def portfolio(request):
    return render(request, 'portfolio.html')

#Contact Page View
def contact(request):
    return render(request, 'contact.html')
