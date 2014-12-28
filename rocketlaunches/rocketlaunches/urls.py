from django.conf.urls import patterns, include, url
from django.contrib import admin

from rocketapp import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'rocketlaunches.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^$', views.index, name='index'),
	url(r'^$', views.index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
)
