from rest_framework import serializers

from rocketapp.models import Rocket, Launch

class LaunchSerializer(serializers.ModelSerializer):
	rocket_name = serializers.ReadOnlyField(source='rocket.name')
	rocket_manufacturer = serializers.ReadOnlyField(source='rocket.manufacturer')
	rocket_manufacturer_url = serializers.ReadOnlyField(source='rocket.manufacturer_url')

	class Meta:
		model = Launch
		fields = (
			'pk',
			'id',
			'remarks', 
			'status', 
			'orbit', 
			'rocket',
			'rocket_name',
			'payload',
			'payload_purpose',
			'country',
			'customer',
			'customer_url',
			'launch_url',
			'launch_date',
			'rocket_manufacturer',
			'rocket_manufacturer_url')

class RocketSerializer(serializers.ModelSerializer):
	class Meta:
		model = Rocket
		fields = ('id', 'name', 'stages', 'height', 'country')
