from django.core.management.base import BaseCommand, CommandError

from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context


class Command(BaseCommand):

    def handle(self, *args, **options):

        # Get list of active subscribers

        # Are there any launches today?

        # Is this the first of the month?

        # If not, return

        # Foreach

        # If they want a daily alert

        # Otherwise, if first of month, send monthly alert

        plaintext = get_template('emailtemplates/launch.today.txt')
        htmly     = get_template('emailtemplates/launch.today.html')

        d = Context()

        subject, from_email, to = 'hello', 'from@example.com', 'to@example.com'
        text_content = plaintext.render(d)
        html_content = htmly.render(d)
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()