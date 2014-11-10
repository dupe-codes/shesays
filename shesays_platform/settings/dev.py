"""
Settings for local development
"""

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'shesays_dev',
        'USER': 'shesays',
    },
}

EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'
