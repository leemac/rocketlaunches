
Configure the settings properly to match your database settings. These settings are stored in: "RocketLaunches/RocketLaunches/Settings". 

== Migrate ==

python manage.py migrate --settings=rocketlaunches.settings.development

== Import ==

There is a small amount of dummy data that can help you get started:

python manage.py loaddata rockets.json --settings=rocketlaunches.settings.development

python manage.py import_data --settings=rocketlaunches.settings.development

== Run Local Server ==

Nothing fancy here:

python manage.py startserver --settings=rocketlaunches.settings.development

== Building Deployed Assets ==

The frontend is built using r.js:

Run: r.js -o build/build.js

== Starting/Stopping on server ==

fab start_server

fab stop_server

== Symbolic Link for Admin assets == 

On production, we must remap the admin assets using a symbolic link.

sudo ln -s /usr/local/lib/python2.7/dist-packages/django/contrib/admin/static/admin admin

