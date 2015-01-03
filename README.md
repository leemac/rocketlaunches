rocketlaunches
==============

RocketLaunches source code.

This is very alpha at the moment. The following are just my quick notes for now on how to set this up.

== Import Data ==

1. Edit data/launches.csv
2. Run: manage.py import_data

== Build ==

Run: r.js -o build/build.js

== Start ==

fab start_server

== Stop ==

fab stop_server

== Deploy ==

fab stop_server

== Migrate ==

python manage.py migrate --settings=rocketlaunches.settings.production

== Import ==

python manage.py loaddata rockets.json --settings=rocketlaunches.settings.production

python manage.py import_data --settings=rocketlaunches.settings.production


