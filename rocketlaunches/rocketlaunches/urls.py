from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers
from rocketapp import views

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()

urlpatterns = patterns('',
	# Examples:
	# url(r'^$', 'rocketlaunches.views.home', name='home'),
	# url(r'^blog/', include('blog.urls')),
	url(r'^$', views.index, name='index'),
	url(r'^api/launches/', views.launches),
	url(r'^api/rockets/', views.rockets),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)
