from django.core.management.base import BaseCommand, CommandError

from rocketapp.models import Launch, Rocket
from datetime import datetime

import csv

class Command(BaseCommand):

    def handle(self, *args, **options):

        f = open("../data/launches.csv", 'rt')

        try:
            reader = csv.DictReader(f)
            for row in reader:
                # Find existing launch record
                rocketName = row['Rocket'];

                if row['LaunchTime']:
                    date = datetime.strptime(row['LaunchDate'] + ' ' + row['LaunchTime'], '%Y-%m-%d %H:%M');
                else:
                    date = datetime.strptime(row['LaunchDate'], '%Y-%m-%d');

                try:

                    existinglaunch = Launch.objects.get(rocket__name=rocketName, launch_date=date)
                    # If Exists, delete it
                    if existinglaunch:
                        existinglaunch.delete()

                except Launch.DoesNotExist:
                    print('Does Not Exist!')

                newLaunch = Launch()

                # Add launch
                
                # Get Rocket
                rocket = Rocket.objects.get(name=rocketName)

                newLaunch.rocket = rocket
                newLaunch.launch_date = date
                newLaunch.payload = row['Payload']
                newLaunch.payload_purpose = row['PayloadPurpose']
                newLaunch.country = row['Country']
                newLaunch.launch_url = row['LaunchVideo']
                newLaunch.status = row['Status']
                newLaunch.remarks = row['Remarks']
                newLaunch.orbit = row['Orbit']

                newLaunch.save()

        finally:
            f.close()