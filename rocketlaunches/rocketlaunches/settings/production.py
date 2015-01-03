from rocketlaunches.settings.base import *

DEBUG = False

ALLOWED_HOSTS = [
	'rocketlaunches.org',
	'www.rocketlaunches.org'
]

DATABASES = {
   'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'rocketlaunches', 
        'USER': 'postgres',
        'PASSWORD': 'test',
        'HOST': 'localhost',    
        'PORT': '',  
    }
}