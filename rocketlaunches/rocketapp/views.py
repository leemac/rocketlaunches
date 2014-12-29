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
   		rawData = Launch.objects.all()

   		# Create array
   		json_res = []

   		# Iterate over results and add to array
   		for record in rawData: 
   			json_res.append(record.as_dict())

		# Return the results   		
   		return HttpResponse(json.dumps(json_res), content_type='application/json')