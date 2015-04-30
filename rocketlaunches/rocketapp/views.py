from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from django.template import RequestContext, loader
from datetime import datetime, timedelta, time

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from rocketlaunches.serializers import LaunchSerializer, RocketSerializer, SubscriberSerializer
from rocketapp.models import Rocket, Launch, Subscriber, Payload

def index(request):
	launches = Launch.objects.all().filter(launch_date__gte=timezone.localtime(timezone.now())).order_by('launch_date')

	template = loader.get_template('index.html')
	context = RequestContext(request, {
		'launches': launches,
	})
	
	return HttpResponse(template.render(context))

@csrf_exempt
def launches(request):
	launches = Launch.objects.all().order_by('-launch_date')

	template = loader.get_template('launches/index.html')
	context = RequestContext(request, {
		'launches': launches,
	})

	return HttpResponse(template.render(context))

@csrf_exempt
def launches_view(request, id):
	launch = Launch.objects.get(pk=id)

	template = loader.get_template('launches/single.html')
	context = RequestContext(request, {
		'launch': launch
	})

	return HttpResponse(template.render(context))

@csrf_exempt
def payloads(request):
	payloads = Payload.objects.all()

	template = loader.get_template('payloads/index.html')
	context = RequestContext(request, {
		'payloads': payloads,
	})

	return HttpResponse(template.render(context))

@csrf_exempt
def payloads_view(request, id):
	payload = Payload.objects.get(id=id)

	template = loader.get_template('payloads/single.html')
	context = RequestContext(request, {
		'payload': payload,
	})

	return HttpResponse(template.render(context))

@csrf_exempt
def rockets(request):
	rockets = Rocket.objects.all().order_by('name')

	template = loader.get_template('rockets/index.html')
	context = RequestContext(request, {
		'rockets': rockets,
	})

	return HttpResponse(template.render(context))

@csrf_exempt
def rockets_view(request, id):
	rocket = Rocket.objects.get(id=id)

	template = loader.get_template('rockets/single.html')
	context = RequestContext(request, {
		'rocket': rocket,
	})

	return HttpResponse(template.render(context))

def about(request):
	template = loader.get_template('about.html')
	context = RequestContext(request)

	return HttpResponse(template.render(context))

@csrf_exempt
def subscribers(request):
	if request.method == 'POST':
		data = JSONParser().parse(request)

		subscriber = Subscriber()
		serializer = SubscriberSerializer(subscriber, data=data)

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