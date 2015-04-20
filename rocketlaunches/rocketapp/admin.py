from django.contrib import admin
from rocketapp.models import Launch, Rocket, Subscriber

# Register your models here.

admin.site.register(Launch)
admin.site.register(Rocket)
admin.site.register(Subscriber)