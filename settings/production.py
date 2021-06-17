from .base import *
DEBUG = True

ALLOWED_HOSTS = ['djangoblogdeve.herokuapp.com' ]

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd1la88lq6diov8',
        'USER':'chvikglmmnrcxu',
        'PASSWORD':'a35bb54b2a5bd0ca24307463ecb05796bc41c3c13cc3b84a9da2cafac9f171a1',
        'HOST':'ec2-54-163-97-228.compute-1.amazonaws.com',
        'PORT':5432,
    }
}

