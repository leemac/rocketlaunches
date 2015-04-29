from django import template
from datetime import datetime, timedelta
from django.utils import timezone
from django.contrib.humanize.templatetags import humanize


register = template.Library()

@register.filter(name='get_launch_displaytext')
def get_launch_displaytext(value):
	return humanize.naturaltime(value)

@register.filter(name='get_launch_displaytext_extra')
def get_launch_displaytext_extra(launch):
	today = timezone.now()

	if launch.launch_date > today:
		theTime = launch.launch_date.strftime('%A %B %e %y at %l:%M %p')
		html = "<br/><small title='" + theTime + "'>" + theTime + " Local Time</small>"

		return humanize.naturaltime(html)
	else:
		return ""