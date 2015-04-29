from django import template
from datetime import datetime, timedelta
from django.utils import timezone
from django.contrib.humanize.templatetags import humanize


register = template.Library()

@register.filter(name='get_launch_displaytext')
def get_launch_displaytext(value):
	today = timezone.now()

	if value > today:
		return humanize.naturaltime(value)
	elif value < today:
		delta = today - value;
		isRecent = delta.days == 3

		if isRecent:
			return humanize.naturaltime(value)
		else:
			return value.strftime('%A %B %e %y at %l:%M %p')

	else:
		return "Nothing"

@register.filter(name='get_launch_displaytext_extra')
def get_launch_displaytext_extra(launch):
	today = timezone.now()

	if launch.launch_date > today:
		theTime = launch.launch_date.strftime('%A %B %e %y at %l:%M %p')
		html = "<br/><small title='" + theTime + "'>" + theTime + " Local Time</small>"

		return humanize.naturaltime(html)
	else:
		return ""