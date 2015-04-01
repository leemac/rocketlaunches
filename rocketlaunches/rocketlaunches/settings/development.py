from rocketlaunches.settings.base import *

DEBUG = True

ALLOWED_HOSTS = [
	'127.0.0.1',
	'localhost'
]

DATABASES = {
   'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'gardentracker', 
        'USER': 'test',
        'PASSWORD': 'test',
        'HOST': 'localhost',    
        'PORT': '',  
    }
}