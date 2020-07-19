import os
import platform

from django.utils.crypto import get_random_string


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = get_random_string(length=50)
if platform.node() == 'wynne':
    DEBUG = True
else:
    DEBUG = False

ALLOWED_HOSTS = [
    '.localhost',
    '127.0.0.1',
    'renenutet.flowerysong.com',
]

INSTALLED_APPS = [
    'api.apps.ApiConfig',
    'ui.apps.UiConfig',
    'mptt',
    'rest_framework',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'renenutet.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
    {
        'BACKEND': 'django.template.backends.jinja2.Jinja2',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'environment': 'renenutet.jinja.environment',
        },
    },
]

WSGI_APPLICATION = 'renenutet.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
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


LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'America/Detroit'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = '/static/'
if platform.node() == 'wynne':
    MEDIA_ROOT = '/home/zeke/git/renenutet/uploads'
else:
    MEDIA_ROOT = '/srv/www/renenutet.flowerysong.com/uploads'
MEDIA_URL = 'uploads/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
