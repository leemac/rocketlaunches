from django.contrib import admin
from rocketapp.models import Launch, Rocket, Subscriber, Payload, Organization, LaunchArticle, LaunchVideo, PayloadVideo, Manufacturer, PayloadFamily, RocketFamily

# Register your models here.

admin.site.register(Manufacturer)
admin.site.register(Launch)
admin.site.register(RocketFamily)
admin.site.register(Rocket)
admin.site.register(PayloadFamily)
admin.site.register(Payload)
admin.site.register(Organization)
admin.site.register(LaunchArticle)
admin.site.register(LaunchVideo)
admin.site.register(PayloadVideo)