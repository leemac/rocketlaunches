from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core import serializers

from rocketapp.models import Launch

import json

def index(request):
   return render(request, 'index.html')

def launches(request):
   if request.method == 'GET':
   		# Get the objects from the database
   		rawData = Launch.objects.all().order_by('-launch_date')
		   
   		return HttpResponse(serializers.serialize('json', rawData), content_type='application/json')