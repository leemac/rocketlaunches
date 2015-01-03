from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers

from rocketlaunches.viewsets import LaunchViewSet, RocketViewSet

from rocketapp import views

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'launches', LaunchViewSet)
router.register(r'rockets', RocketViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'rocketlaunches.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^$', views.comingsoon, name='comingsoon'),
    url(r'^api/', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)
