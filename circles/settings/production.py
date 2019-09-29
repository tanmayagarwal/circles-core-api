from os import environ

from .base import *

DEBUG = False


'''DATABASE CONFIGURATION'''
DATABASES = {
    'default': {
        'ENGINE': environ.get('CIRCLES_DB_ENGINE', ''),
        'NAME': environ.get('CIRCLES_DB_NAME', ''),
        'USER': environ.get('CIRCLES_DB_USER', ''),
        'PASSWORD': environ.get('CIRCLES_DB_PASSWORD', ''),
        'HOST': environ.get('CIRCLES_DB_HOST', ''),
        'PORT': environ.get('CIRCLES_DB_PORT', ''),
    }
}

