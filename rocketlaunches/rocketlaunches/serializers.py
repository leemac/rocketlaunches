from rest_framework import serializers

from rocketapp.models import Rocket, Launch, Subscriber

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
			'launch_date_tbd',
			'rocket_manufacturer',
			'rocket_manufacturer_url')

class RocketSerializer(serializers.ModelSerializer):

	cost = serializers.FloatField()

	class Meta:
		model = Rocket
		fields = (
			'id', 
			'name', 
			'stages', 
			'height', 
			'country',
			'mass',
			'diameter',
			'payload_to_leo',
			'payload_to_sso',
			'status',
			'wiki_url',
			'cost',
			'rocket_function',
			'cost_year',
			'first_flight_date',
			'manufacturer',
			'manufacturer_url')

class SubscriberSerializer(serializers.ModelSerializer):

	class Meta:
		model = Subscriber
		fields = (
			'id', 
			'email')
