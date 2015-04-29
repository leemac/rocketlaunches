from rocketlaunches.settings.base import *

DEBUG = True

ALLOWED_HOSTS = [
	'127.0.0.1',
	'localhost'
]

DATABASES = {
   'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'rocketlaunches', 
        'USER': 'test',
        'PASSWORD': 'test',
        'HOST': '127.0.0.1',    
        'PORT': '5432',  
    }
}

SITEOFFLINE = True

EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = '/tmp/rocket-messages' # change this to a proper location