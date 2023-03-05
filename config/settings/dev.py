"""Development settings."""

import datetime
from .base import *  # NOQA
from .base import env
import os

# Base
DEBUG = env.bool('MARKETPLACE_DJANGO_DEBUG')

# Security
SECRET_KEY = env.str('MARKETPLACE_DJANGO_SECRET_KEY')
ALLOWED_HOSTS = [
    "*"
]

INTERNAL_IPS = (
    "*"
)

CORS_ORIGIN_WHITELIST = [
    "*",
]

CSRF_TRUSTED_ORIGINS = [
    'https://4924-81-38-122-210.eu.ngrok.io/'
    '*',
]


# Templates
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG  # NOQA

AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
]

if MARKETPLACE_DEBUG_TOOLBAR:
    INSTALLED_APPS += ['debug_toolbar']
    MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']
    import socket  # only if you haven't already imported this
    hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
    INTERNAL_IPS = [
        ip[: ip.rfind(".")] + ".1" for ip in ips] + ["127.0.0.1", "10.0.2.2"]
