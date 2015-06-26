from django.db import models
from datetime import datetime, date

class Manufacturer(models.Model):
	name = models.CharField(max_length=200)
	country = models.CharField(max_length=10, blank=True, null=True)
	url = models.CharField(max_length=2000, null=True, blank=True)
	wiki_url = models.CharField(max_length=2000, blank=True, null=True)
	description = models.CharField(max_length=2000, blank=True, null=True)

	def __str__(self):
		return self.name

class RocketFamily(models.Model):
	name = models.CharField(max_length=200)
	description = models.CharField(max_length=2000, blank=True, null=True)

	def __str__(self):
		return self.name

class Rocket(models.Model):
	rocket_family = models.ForeignKey(RocketFamily, default='', null=True, blank=True)
	name = models.CharField(max_length=200)
	stages = models.IntegerField()
	height = models.DecimalField(max_digits=8, decimal_places=2)
	mass = models.DecimalField(max_digits=8, decimal_places=2)
	diameter = models.DecimalField(max_digits=8, decimal_places=2)
	cost = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
	cost_year = models.IntegerField(null=True, blank=True)
	manufacturers = models.ManyToManyField(Manufacturer)
	payload_to_leo = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
	payload_to_gto = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
	payload_to_sso = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
	payload_to_gso = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
	status = models.CharField(max_length=200)
	first_flight_date = models.DateTimeField(blank=True, null=True)
	wiki_url = models.CharField(max_length=1000)
	rocket_function = models.CharField(max_length=1000)
	description = models.CharField(max_length=1000, null=True, blank=True)
	country = models.CharField(max_length=10, blank=False)
	created_date = models.DateTimeField('date created', default=datetime.now())
	updated_date = models.DateTimeField('date updated', blank=True, null=True)

	def __str__(self):
		return self.name

class PayloadFamily(models.Model):
	name = models.CharField(max_length=200)

	def __str__(self):
		return self.name

class Payload(models.Model):
	payload_family = models.ForeignKey(PayloadFamily, default='', null=True, blank=True)
	name = models.CharField(max_length=200)
	url = models.CharField(max_length=2000, null=True, blank=True)
	wiki_url = models.CharField(max_length=2000, null=True, blank=True)
	description = models.CharField(max_length=2000, null=True, blank=True)
	manufacturers = models.ManyToManyField(Manufacturer)

	def __str__(self):
		return self.name

class Launch(models.Model):
	country = models.CharField(max_length=10, blank=False, null=False, default='')
	rocket = models.ForeignKey(Rocket, default='', related_name='launches')
	payloads = models.ManyToManyField(Payload, default='')
	remarks = models.CharField(max_length=2000, blank=True, null=True)
	customer = models.CharField(max_length=2000, blank=True, null=True)
	customer_url = models.CharField(max_length=2000, blank=True, null=True)
	payload = models.CharField(max_length=2000, blank=True, null=True)
	payload_purpose = models.CharField(max_length=2000, blank=True, null=True)
	status = models.CharField(max_length=2000, blank=False, null=False, default='')
	status_url = models.CharField(max_length=2000, blank=True, null=True)
	launch_url = models.CharField(max_length=2000, blank=True, null=True)
	orbit = models.CharField(max_length=100, blank=True, null=True)
	launch_date = models.DateTimeField('date launched', blank=True, null=True)
	launch_date_tbd = models.NullBooleanField(blank=True, null=True)
	created_date = models.DateTimeField('date created', default=datetime.now())
	updated_date = models.DateTimeField('date updated', blank=True, null=True)

	def __str__(self):
		return self.rocket.name + ' ' + str(self.launch_date)

class Organization(models.Model):
	name = models.CharField(max_length=200)
	url = models.CharField(max_length=2000)
	wiki_url = models.CharField(max_length=2000)
	description = models.CharField(max_length=2000)

	def __str__(self):
		return self.name

class Subscriber(models.Model):
	email = models.CharField(max_length=200, blank=False, null=False, default='')
	active = models.BooleanField(blank=False, null=False, default=True)
	created_date = models.DateTimeField('date created', default=datetime.now())
	updated_date = models.DateTimeField('date updated', blank=True, null=True)

	def __str__(self):
		return self.email

class LaunchArticle(models.Model):
	text = models.CharField(max_length=200)
	url = models.CharField(max_length=2000)
	launch = models.ForeignKey(Launch, default='')

	def __str__(self):
		return self.text

class LaunchVideo(models.Model):
	text = models.CharField(max_length=200)
	url = models.CharField(max_length=2000)
	description = models.CharField(max_length=2000)
	launch = models.ForeignKey(Launch, default='')

	def __str__(self):
		return self.text

class PayloadVideo(models.Model):
	text = models.CharField(max_length=200)
	url = models.CharField(max_length=2000)
	description = models.CharField(max_length=2000)
	payload = models.ForeignKey(Payload, default='')

	def __str__(self):
		return self.text