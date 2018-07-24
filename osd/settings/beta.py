from .base import *
from .secret_beta import *

DEBUG = True

ALLOWED_HOSTS = ['www.greenpen.net',
                 'jdjwright.pythonanywhere.com',
                 'localhost'
]

SECURE_SSL_REDIRECT = True


STATIC_URL = '/static/'
STATIC_ROOT = '/home/greenpen/osd-beta/OSD/static'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
