from .base import *

SECRET_KEY = '*+3s!e@j!#yzclaf4z7vct&p7qobgm#8ja3vy(9%6agn#v&37#'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, '../../db.sqlite3'),
    }
}