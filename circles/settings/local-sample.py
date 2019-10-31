from os import environ
import os
from .base import *

DEBUG = True


'''DATABASE CONFIGURATION'''
DATABASES = {
    'default': {
        'ENGINE': os.environ.get('CIRCLES_DB_ENGINE', 'django.db.backends.sqlite3'),
        'NAME': os.environ.get('CIRCLES_DB_NAME', 'db'),
        'USER': os.environ.get('CIRCLES_DB_USER', 'postgres'),
        'PASSWORD': os.environ.get('CIRCLES_DB_PASSWORD', 'postgres'),
        'HOST': os.environ.get('CIRCLES_DB_HOST', 'localhost'),
        'PORT': os.environ.get('CIRCLES_DB_PORT', '5432'),
    }
}

ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS").split(" ")

# Use nose to run all tests
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

# Tell nose to measure coverage on the 'foo' and 'bar' apps
NOSE_ARGS = [
    '--with-coverage',
    '--cover-package=foo,bar',
]
