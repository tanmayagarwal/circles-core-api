from os import environ
import os
from .base import *

DEBUG = True


'''DATABASE CONFIGURATION'''
DATABASES = {
    'default': {
        'ENGINE': os.environ.get('CIRCLES_DB_ENGINE', ''),
        'NAME': os.environ.get('CIRCLES_DB_NAME', ''),
        'USER': os.environ.get('CIRCLES_DB_USER', ''),
        'PASSWORD': os.environ.get('CIRCLES_DB_PASSWORD', ''),
        'HOST': os.environ.get('CIRCLES_DB_HOST', ''),
        'PORT': os.environ.get('CIRCLES_DB_PORT', ''),
    }
}


# Use nose to run all tests
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

# Tell nose to measure coverage on the 'foo' and 'bar' apps
NOSE_ARGS = [
    '--with-coverage',
    '--cover-package=foo,bar',
]
