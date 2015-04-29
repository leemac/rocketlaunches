from django.contrib import admin
from rocketapp.models import Launch, Rocket, Subscriber, Payload, Organization, LaunchArticle, LaunchVideo, PayloadVideo, Manufacturer

# Register your models here.

admin.site.register(Launch)
admin.site.register(Rocket)
admin.site.register(Payload)
admin.site.register(Organization)
admin.site.register(LaunchArticle)
admin.site.register(LaunchVideo)
admin.site.register(PayloadVideo)
admin.site.register(Manufacturer)