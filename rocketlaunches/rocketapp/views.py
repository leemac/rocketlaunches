from django.shortcuts import render

from rocketapp.models import Launch

def index(request):
   return render(request, 'index.html')