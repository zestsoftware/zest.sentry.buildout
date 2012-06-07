import os
here = lambda *x: os.path.join(os.path.abspath(os.path.dirname(__file__)), *x)

import os.path

CONF_ROOT = os.path.dirname(__file__)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': here('..', 'central_sentry.db'), # Or path to database file if using sqlite3.
    }
}

SENTRY_KEY = 'HEiISJcx80odku6QUZp3++aLtS6wJlDs780+24GsUhFIZGJ5bUhvHg=='

# Set this to false to require authentication
SENTRY_PUBLIC = True

# You should configure the absolute URI to Sentry. It will attempt to guess it if you don't
# but proxies may interfere with this.
# SENTRY_URL_PREFIX = 'http://sentry.example.com'  # No trailing slash!

SENTRY_URL_PREFIX = 'http://sentry.zestsoftware.nl'

SENTRY_WEB_HOST = '0.0.0.0'
SENTRY_WEB_PORT = 16130
SENTRY_WEB_OPTIONS = {
    'workers': 3,  # the number of gunicorn workers
    # 'worker_class': 'gevent',
}

# Mail server configuration

# For more information check Django's documentation:
#  https://docs.djangoproject.com/en/1.3/topics/email/?from=olddocs#e-mail-backends

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = 'localhost'
EMAIL_HOST_PASSWORD = ''
EMAIL_HOST_USER = ''
EMAIL_PORT = 25
EMAIL_USE_TLS = False
