from django.contrib import messages
from django.shortcuts import render, redirect

from app.models import Contact


# Create your views here.
def home(request):
    context = {
        'title': 'Welcome'
    }
    return render(request, 'index.html', context)
#