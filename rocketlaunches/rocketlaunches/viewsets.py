from rest_framework import viewsets

from rocketlaunches.serializers import LaunchSerializer, RocketSerializer
from rocketapp.models import Rocket, Launch
from datetime import datetime, timedelta, time

class LaunchViewSet(viewsets.ModelViewSet):
	model = Launch
	serializer_class = LaunchSerializer

	def get_queryset(self):
		queryset = Launch.objects.all().order_by('-launch_date')

		type = self.request.QUERY_PARAMS.get('type', None)

		if type:
			today = datetime.now().date()
			today_start = datetime.combine(today, time())

			if type == "upcoming":		
				queryset = Launch.objects.all().filter(launch_date__gte=today_start).order_by('launch_date')
			else:
				queryset = Launch.objects.all().filter(launch_date__lte=today_start).order_by('-launch_date')

		return queryset

class RocketViewSet(viewsets.ModelViewSet):
	queryset = Rocket.objects.all()
	serializer_class = RocketSerializer