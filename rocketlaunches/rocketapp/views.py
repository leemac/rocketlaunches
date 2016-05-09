from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from django.template import RequestContext, loader
from datetime import datetime, timedelta, time

#from rest_framework.renderers import JSONRenderer
#from rest_framework.parsers import JSONParser

#from rocketlaunches.serializers import LaunchSerializer, RocketSerializer, SubscriberSerializer
from rocketapp.models import Rocket, Launch, Subscriber, Payload

def index(request):
	launches = Launch.objects.all().filter(launch_date__gte=timezone.localtime(timezone.now())).order_by('launch_date')

	template = loader.get_template('index.html')
	context = RequestContext(request, {
		'launches': launches,
		'navlocation': 'home',
	})
	
	return HttpResponse(template.render(context))
