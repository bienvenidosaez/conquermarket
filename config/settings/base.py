import environ
from pathlib import Path
import os
from django.urls import reverse_lazy

env = environ.Env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
ROOT_DIR = environ.Path(__file__) - 3
APPS_DIR = ROOT_DIR.path("marketplace")

DEV = env.bool('MARKETPLACE_DJANGO_DEV')
DEVJS = env.bool('MARKETPLACE_DJANGO_DEVJS')
MARKETPLACE_DEBUG_TOOLBAR = env.bool('MARKETPLACE_DEBUG_TOOLBAR', False)


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '9mgu=0t7adojsh2zgkfn2kw(a!@ob(t^3f6ebch3_q7(2=yn)v'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool("MARKETPLACE_DJANGO_DEBUG")

ALLOWED_HOSTS = []

# Language and timezone
TIME_ZONE = "Europe/Madrid"
LANGUAGE_CODE = 'es-ES'
USE_L10N = True
USE_I18N = True
USE_TZ = True

prefix_default_language = False


def gettext(s):
    return s


LANGUAGES = (
    ("en", gettext("English")),
    ("es", gettext("Spanish")),
)

# Application definition

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_PARTY_APPS = [
    "crispy_forms",
    'django_extensions',
    'django_filters',
    'corsheaders',
    'rest_framework',
]

LOCAL_APPS = [
    'buyers',
    'products'
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

WSGI_APPLICATION = 'config.wsgi.application'

# DATABASES
DATABASES = {
    "default": env.db("DATABASE_URL"),
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LOCALE_PATHS = [
    os.path.join(BASE_DIR, '_locale'),
]

STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

STATIC_ROOT = str(ROOT_DIR("staticfiles"))
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    str(ROOT_DIR.path("marketplace").path('static')),
]

# Media
MEDIA_ROOT = "/marketplace-media"
MEDIA_URL = "/media/"

CRISPY_TEMPLATE_PACK = 'bootstrap4'

TEMPLATES_DIR = str(APPS_DIR.path("_templates"))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR, ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'builtins': [
                'django.templatetags.static',
            ]
        },
    },
]


# Admin
ADMIN_URL = "admin/"
ADMINS = [
    ("""Bienvenido Sáez Muelas""", "bienvenidosaez@baetica.com"),
]
MANAGERS = ADMINS

LOCALE_PATHS = (str(APPS_DIR.path("locale")),)

USE_I18N = True
USE_L10N = True
LANGUAGE_CODE = "es-ES"

LOGIN_REDIRECT_URL = "/"

AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
]

# URL config
SITE_URL = env.str("MARKETPLACE_SITE_URL")

FILE_UPLOAD_PERMISSIONS = 0o640  # De audax
LOGIN_REDIRECT_URL = "/"

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    # 'DEFAULT_PERMISSION_CLASSES': [
    #     'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    # ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 99999,
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    # 'DEFAULT_RENDERER_CLASSES': (
    #     'rest_framework.renderers.JSONRenderer',
    # ),
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ],
}

CORS_ALLOWED_ORIGINS = [
    'http://localhost:8000',
    'http://localhost:3000',
    'http://conquermarket.38018.net',
    'http://conquermarket.34018.net:3000',
    'http://conquermarket.34018.net:8000',
]

CSRF_TRUSTED_ORIGINS = [
    'http://localhost:8000',
    'http://localhost:3000',
    'http://conquermarket.38018.net',
    'conquermarket.38018.net',
    'localhost:8000',
    'localhost:3000',
    'http://conquermarket.34018.net:3000',
    'http://conquermarket.34018.net:8000',
    '*'
]

ALLOWED_HOSTS = [
    'http://localhost:8000',
    'http://localhost:3000',
    'http://conquermarket.38018.net',
    'conquermarket.38018.net',
    'localhost:8000',
    'localhost:3000',
    'http://conquermarket.34018.net:3000',
    'http://conquermarket.34018.net:8000',
    '*'

]

# If this is used then `CORS_ALLOWED_ORIGINS` will not have any effect
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True

# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
