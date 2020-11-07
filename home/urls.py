from django.contrib import admin 
from django.urls import path, include
from home.views import home, about, resume, portfolio, contact

urlpatterns = [
    path('', home , name = 'home'),
    path('about', about , name = 'about'),
    path('resume', resume , name = 'resume'),
    path('portfolio', portfolio , name = 'portfolio'),
    path('contact', contact, name = 'contact'),
]
