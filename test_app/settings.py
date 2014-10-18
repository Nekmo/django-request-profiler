
DEBUG = True
TEMPLATE_DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'test_db'
    }
}

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_coverage',
    'request_profiler',
    'test_app',
    'south'
)

MIDDLEWARE_CLASSES = [
    # this package's middleware
    'request_profiler.middleware.ProfilingMiddleware',

    # default django middleware
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
]

TEMPLATE_CONTEXT_PROCESSORS = [
    'django.contrib.messages.context_processors.messages',
    'django.contrib.auth.context_processors.auth',
]

STATIC_URL = "/static/"

SECRET_KEY = "secret"

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'propagate': True,
            'level': 'DEBUG',
        },
        'django': {
            'handlers': ['console'],
            'propagate': True,
            'level': 'INFO',
        },
        'request_profiler': {
            'handlers': ['console'],
            'propagate': True,
            'level': 'DEBUG',
        },
    }
}

ROOT_URLCONF = 'test_app.urls'

###################################################
# django_coverage overrides

# Specify a list of regular expressions of module paths to exclude
# from the coverage analysis. Examples are ``'tests$'`` and ``'urls$'``.
# This setting is optional.
COVERAGE_MODULE_EXCLUDES = [
    'tests$',
    'settings$',
    'urls$',
    'locale$',
    'common.views.test',
    '__init__',
    'django',
    'migrations',
    'request_profiler.admin',
    'request_profiler.signals',
]
COVERAGE_REPORT_HTML_OUTPUT_DIR = 'coverage/html'
COVERAGE_USE_STDOUT = True

# turn off caching for tests
REQUEST_PROFILER_RULESET_CACHE_TIMEOUT = 0