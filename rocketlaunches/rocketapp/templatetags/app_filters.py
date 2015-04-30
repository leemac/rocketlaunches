from django import template
from datetime import datetime, timedelta
from django.utils import timezone
from django.contrib.humanize.templatetags import humanize


register = template.Library()

@register.filter(name='get_launch_displaytext')
def get_launch_displaytext(value):
	today = timezone.now()

	if value < today:
		return value.strftime('%A %B %e %y at %l:%M %p')
	else:
		return humanize.naturaltime(value)

@register.filter(name='get_launch_displaytext_extra')
def get_launch_displaytext_extra(value):
	today = timezone.now()

	if value > today:
		theTime = value.strftime('%A %B %e %y at %l:%M %p')
		html = "<br/><small title='" + theTime + "'>" + theTime + " Local Time</small>"

		return humanize.naturaltime(html)
	else:
		return "<br/><small>" + humanize.naturaltime(value) + "</small>"