from django.db import models
from datetime import datetime, date

class Launch(models.Model):
	name = models.CharField(max_length=500)
	launch_date = models.DateTimeField('date launched', blank=True, null=True)
	created_date = models.DateTimeField('date created', default=datetime.now())
	updated_date = models.DateTimeField('date updated', blank=True, null=True)

	def as_dict(self):
	        return dict(
		        name = self.name, 
		        launch_date = self.launch_date,
		        created_date = str(self.created_date),
		        updated_date = str(self.updated_date)
	        )