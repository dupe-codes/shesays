"""
Django settings for shesays project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# To avoid SITE_ID exception
SITE_ID = 1
DOMAIN_NAME = 'shesays.co'
SITE_NAME = 'SheSays'

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-@wbpgamqi4#a8b86&nd(q^2(qhix1au+tgr79dnmjl7$377u%'

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

# List of all SheSays specific Django apps
SHESAYS_APPS = (
    'shesays_platform.apps.home',
    'shesays_platform.apps.companies',
    'shesays_platform.apps.reviews',
    'shesays_platform.apps.utilities',
    'shesays_platform.apps.analytics',
    'shesays_platform.apps.invitations',
)

THIRD_PARTY_APPS = (
    'account',
    'pinax_theme_bootstrap',
    'bootstrapform',
    'django_forms_bootstrap',
    'djcelery',
    'mailer',
    'djcelery_email',
)

DJANGO_DEFAULT_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
)


INSTALLED_APPS = SHESAYS_APPS + THIRD_PARTY_APPS + DJANGO_DEFAULT_APPS

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'account.middleware.LocaleMiddleware',
    'account.middleware.TimezoneMiddleware'
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
    'account.context_processors.account',
    'pinax_theme_bootstrap.context_processors.theme'
)

TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]

ROOT_URLCONF = 'shesays_platform.urls'

WSGI_APPLICATION = 'shesays_platform.wsgi.application'


# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static/'),
)

# Configure Logging

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/info.log'),
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'shesays_platform': {
            'handlers': ['file'],
            'level': 'INFO',
        },
    },
}

# Configuration for async tasks
import djcelery
djcelery.setup_loader()

# Email configuration
EMAIL_BACKEND = 'djcelery_email.backends.CeleryEmailBackend'
DEFAULT_FROM_EMAIL = 'info@shesays.co'

# Email broker settings
BROKER_URL = 'amqp://guest:guest@localhost:5672/'
