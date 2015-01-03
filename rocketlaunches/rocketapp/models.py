from django.db import models
from datetime import datetime, date

class Rocket(models.Model):
	name = models.CharField(max_length=200)
	stages = models.IntegerField()
	height = models.DecimalField(max_digits=8, decimal_places=2)
	mass = models.DecimalField(max_digits=8, decimal_places=2)
	diameter = models.DecimalField(max_digits=8, decimal_places=2)
	cost = models.DecimalField(max_digits=15, decimal_places=2, null=True)
	cost_year = models.IntegerField(null=True)
	payload_to_leo = models.DecimalField(max_digits=8, decimal_places=2, null=True)
	payload_to_gto = models.DecimalField(max_digits=8, decimal_places=2, null=True)
	payload_to_sso = models.DecimalField(max_digits=8, decimal_places=2, null=True)
	payload_to_gso = models.DecimalField(max_digits=8, decimal_places=2, null=True)
	status = models.CharField(max_length=200)
	first_flight_date = models.DateTimeField(blank=True, null=True)
	wiki_url = models.CharField(max_length=1000)
	manufacturer = models.CharField(max_length=1000)
	manufacturer_url = models.CharField(max_length=1000)
	rocket_function = models.CharField(max_length=1000)
	description = models.CharField(max_length=1000)
	country = models.CharField(max_length=10, blank=False)
	created_date = models.DateTimeField('date created', default=datetime.now())
	updated_date = models.DateTimeField('date updated', blank=True, null=True)

	def __str__(self):
		return self.name

class Launch(models.Model):
	country = models.CharField(max_length=10, blank=False, null=False, default='')
	rocket = models.ForeignKey(Rocket, default='')
	remarks = models.CharField(max_length=2000, blank=True, null=True)
	customer = models.CharField(max_length=2000, blank=True, null=True)
	customer_url = models.CharField(max_length=2000, blank=True, null=True)
	payload = models.CharField(max_length=2000, blank=True, null=True)
	status = models.CharField(max_length=2000, blank=False, null=False, default='')
	status_url = models.CharField(max_length=2000, blank=True, null=True)
	launch_url = models.CharField(max_length=2000, blank=True, null=True)
	orbit = models.CharField(max_length=100, blank=True, null=True)
	launch_date = models.DateTimeField('date launched', blank=True, null=True)
	created_date = models.DateTimeField('date created', default=datetime.now())
	updated_date = models.DateTimeField('date updated', blank=True, null=True)
