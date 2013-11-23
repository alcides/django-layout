from settings import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': relative('db/prod.db'),
        'USER': '',
        'PASSWORD': '',
        'HOST': '',                      # empty -> localhost
        'PORT': '',                      # empty -> default
    }
}

ALLOWED_HOSTS = ['*']
