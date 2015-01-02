from rest_framework import viewsets

from rocketlaunches.serializers import LaunchSerializer, RocketSerializer
from rocketapp.models import Rocket, Launch

class LaunchViewSet(viewsets.ModelViewSet):
	queryset = Launch.objects.all().order_by('-launch_date')
	serializer_class = LaunchSerializer

class RocketViewSet(viewsets.ModelViewSet):
	queryset = Rocket.objects.all()
	serializer_class = RocketSerializer