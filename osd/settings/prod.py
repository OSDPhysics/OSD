from .base import *
from .secret import *

DEBUG = False

ALLOWED_HOSTS = ['www.greenpen.net',
]




STATIC_URL = '/static/'
STATIC_ROOT = '/home/greenpen/OSD/static'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATIC_URL = '/static/'
STATIC_ROOT = '/home/greenpen/OSD/static'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')