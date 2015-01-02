from rocketlaunches.settings.base import *

DEBUG = False

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