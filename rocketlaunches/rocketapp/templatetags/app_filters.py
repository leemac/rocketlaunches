from django import template
from datetime import timedelta
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

	if value > today.datetime.utcnow().replace(tzinfo=utc):
		theTime = value.strftime('%A %B %e %y at %l:%M %p')
		html = "<br/><small title='" + theTime + "'>" + theTime + " Local Time</small>"

		return humanize.naturaltime(html)
	else:
		return "<br/><small>" + humanize.naturaltime(value) + "</small>"

@register.simple_tag
def active_page(request, view_name):
    from django.core.urlresolvers import resolve, Resolver404
    if not request:
        return ""
    try:
        return "active" if resolve(request.path_info).url_name == view_name else ""
    except Resolver404:
        return ""