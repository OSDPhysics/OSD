from .base import *

DEBUG = True

ALLOWED_HOSTS = ['localhost','127.0.0.1',
]

SECRET_KEY = '*+3s!e@j!#yzclaf4z7vct&p7qobgm#8ja3vy(9%6agn#v&37#'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, '../../db.sqlite3'),
    }
}