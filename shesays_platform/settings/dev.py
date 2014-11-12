"""
Settings for local development
"""

from base import INSTALLED_APPS

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'shesays_dev',
        'USER': 'shesays',
    },
}

# Development message queue
BROKER_URL = 'django://'
INSTALLED_APPS += ('kombu.transport.django',)

# Settings for the smtp email service
# Right now I'm using my own gmail account, but in production
# we should use Amazon SES
# Also, need to look in to a better way of mocking email
# sending in development
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'njdupp@gmail.com'
EMAIL_HOST_PASSWORD = 'penguincomputerdesignersailing'
EMAIL_PORT = 587
