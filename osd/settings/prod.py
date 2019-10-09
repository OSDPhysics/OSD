from .base import *
from .secret_prod import *

DEBUG = True

ALLOWED_HOSTS = [
                 'greenpen.net',
                 'prod.greenpen.net',
                'localhost'
]

SECURE_SSL_REDIRECT = False


STATIC_URL = '/static/'
STATIC_ROOT = '/home/james/OSD/static'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
