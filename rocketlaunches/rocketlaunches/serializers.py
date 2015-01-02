from rest_framework import routers, serializers, viewsets

from rocketapp.models import Rocket, Launch

# Launch

class LaunchSerializer(serializers.ModelSerializer):
	rocket_name = serializers.ReadOnlyField(source='rocket.name')
	rocket_manufacturer = serializers.ReadOnlyField(source='rocket.manufacturer')

	class Meta:
		model = Launch
		fields = (
			'remarks', 
			'status', 
			'orbit', 
			'rocket_name',
			'payload',
			'country',
			'launch_url',
			'launch_date',
			'rocket_manufacturer')

class LaunchViewSet(viewsets.ModelViewSet):
	queryset = Launch.objects.all()
	serializer_class = LaunchSerializer

# Rocket

class RocketSerializer(serializers.ModelSerializer):
	class Meta:
		model = Rocket
		fields = ('name', 'stages', 'height')

class RocketViewSet(viewsets.ModelViewSet):
	queryset = Rocket.objects.all()
	serializer_class = RocketSerializer