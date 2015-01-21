from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from rocketlaunches.serializers import LaunchSerializer, RocketSerializer
from rocketapp.models import Rocket, Launch
from datetime import datetime, timedelta, time
from django.utils import timezone


from rocketapp.models import Launch

def index(request):
   return render(request, 'index.html')

@csrf_exempt
def launches(request):

	if request.method == 'GET':
		launches = Launch.objects.all().order_by('-launch_date')

		type = 	request.GET['type']

		if type:
			if type == "upcoming":		
				launches = Launch.objects.all().filter(launch_date__gte=timezone.localtime(timezone.now())).order_by('launch_date')
			else:
				launches = Launch.objects.all().filter(launch_date__lte=timezone.localtime(timezone.now())).order_by('-launch_date')

		serializer = LaunchSerializer(launches, many=True)
		return JSONResponse(serializer.data)

	if request.method == 'DELETE':
		data = JSONParser().parse(request)
		pk = data['pk']

		try:
			launch = Launch.objects.get(pk=pk)
		except Launch.DoesNotExist:
			return HttpResponse(status=404)

		launch.delete()

		return HttpResponse()

	if request.method == 'PUT':
		
		data = JSONParser().parse(request)
		pk = data['pk']

		try:
			launch = Launch.objects.get(pk=pk)
		except Launch.DoesNotExist:
			return HttpResponse(status=404)

		serializer = LaunchSerializer(launch, data=data)

		if serializer.is_valid():
			serializer.save()

			return JSONResponse(serializer.data, status=201)

		return JSONResponse(serializer.errors, status=400)

def rockets(request):
	if request.method == 'GET':
		rockets = Rocket.objects.all().order_by('name')
		serializer = RocketSerializer(rockets, many=True)
	
		return JSONResponse(serializer.data)

	if request.method == 'PUT':	

		data = JSONParser().parse(request)
		serializer = RocketSerializer(data=data)

		if serializer.is_valid():
			serializer.save()
			return JSONResponse(serializer.data, status=201)

		return JSONResponse(serializer.errors, status=400)

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)