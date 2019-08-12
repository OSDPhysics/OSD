from .base import *
from .secret_dev import SOCIAL_AUTH_GOOGLE_OAUTH2_KEY, SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET

DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1',
]

SECRET_KEY = '*+3s!e@j!#yzclaf4z7vct&p7qobgm#8ja3vy(9%6agn#v&37#'

DATABASES = {
     'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'greenpen_dev',
        'USER': 'greenpen',
        'PASSWORD': 'OArFj5vznKbFBf2J6U',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
