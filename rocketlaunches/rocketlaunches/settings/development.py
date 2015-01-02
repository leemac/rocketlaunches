from jobsite.settings.base import *

DEBUG = True

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