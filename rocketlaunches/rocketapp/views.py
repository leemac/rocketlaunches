from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from rocketapp.models import Launch

def index(request):
   return render(request, 'index.html')

def comingsoon(request):
   return render(request, 'comingsoon.html')