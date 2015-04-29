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
	url(r'^$', views.index, name='home'),
	url(r'^launches/(?P<id>[0-9]+)/$', views.launches_view, name='launches_view'),
	url(r'^rockets/(?P<id>[0-9]+)/$', views.rockets_view, name='rockets_view'),
	url(r'^payloads/(?P<id>[0-9]+)/$', views.payloads_view, name='payloads_view'),

	url(r'^launches/', views.launches, name='launches'),
	url(r'^rockets/', views.rockets, name='rockets'),
	url(r'^payloads/', views.payloads, name='payloads'),
	
	url(r'^about/', views.about, name='about'),
	url(r'^api/subscribers/', views.subscribers),
	url(r'^api/launches/', views.launches),
	url(r'^api/rockets/', views.rockets),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)
