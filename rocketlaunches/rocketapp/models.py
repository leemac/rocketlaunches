from django.db import models
from datetime import datetime

class Launch(models.Model):
	name = models.CharField(max_length=500)
	launch_date = models.DateTimeField('date launched', blank=True, null=True)
	created_date = models.DateTimeField('date created', default=datetime.now())
	updated_date = models.DateTimeField('date updated', blank=True, null=True)

	def __str__(self):
		return self.name