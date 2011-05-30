import os, platform

DEVELOPMENT_MODE = (platform.node() != "uhura.websushi.org")
PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))

DEFAULT_FROM_EMAIL = "info@django-de.org"

ADMINS = (
    ('Arne Brodowski', 'arne@rcs4u.de'),
    ('Jannis Leidel', 'jannis@leidel.info'),
    ('Martin Mahner', 'martin@mahner.org'),
)

MANAGERS = ADMINS

if DEVELOPMENT_MODE:
    DEBUG = True
    PREPEND_WWW = False
    CACHE_BACKEND = "file:///tmp/"
    DATABASE_ENGINE = 'sqlite3'
    DATABASE_NAME = os.path.join(PROJECT_PATH, 'django_de.db')
    SECRET_KEY = 'a1o#rz$vv6i$ptm-86h^r7n@v#v!h-@4+gh1e$@jf+b+li4z$*'
else:
    DEBUG = False
    PREPEND_WWW = True
    try:
        from local_settings import *
    except ImportError:
        pass

TEMPLATE_DEBUG = DEBUG

# Local time zone for this installation. All choices can be found here:
# http://www.postgresql.org/docs/current/static/datetime-keywords.html#DATETIME-TIMEZONE-SET-TABLE
TIME_ZONE = 'Europe/Berlin'

# Language code for this installation. All choices can be found here:
# http://www.w3.org/TR/REC-html40/struct/dirlang.html#langcodes
# http://blogs.law.harvard.edu/tech/stories/storyReader$15
LANGUAGE_CODE = 'de'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = '/home/django-de/lib/django_de/site_media/'

# URL that handles the media served from MEDIA_ROOT.
# Example: "http://media.lawrence.com"
MEDIA_URL = '/site_media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/admin_media/'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.csrf.middleware.CsrfMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    #'django.middleware.cache.CacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'pagination.middleware.PaginationMiddleware',
)

ROOT_URLCONF = 'django_de.urls'

TEMPLATE_DIRS = [os.path.join(PROJECT_PATH, 'templates')]

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.sitemaps',
    'django_de.apps.authors',
    'django_de.apps.aggregator',
    'django_de.apps.jobboard',
    'django_de.apps.ticker',
    'pagination',
    'tagging',
    'threadedcomments',
    'django_extensions',
    'robots',
)


TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.auth',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
    'django_de.apps.ticker.context_processors.popular_tags',
)

# ############################################################################
# Aggregator Settings
# ############################################################################
# Nach wie vielen Fehlversuchen (404, Feed kaputt etc.) soll der Feed als
# "nicht public" markiert werden
AGGREGATOR_MAX_ERRORS = 24

# The path to your default gravatar-image under `MEDIA_URL`
AGGREGATOR_GRAVATAR_DEFAULT_IMAGE = 'theme/gravatar.png'

# Gravatar image size
AGGREGATOR_GRAVATAR_SIZE = 50

# Gravatar Rating; must be one of [ G | PG | R | X ]
AGGREGATOR_GRAVATAR_RATING = 'PG'


# ############################################################################
# Pagination
# ############################################################################

PAGINATION_DEFAULT_PAGINATION = 10
PAGINATION_DEFAULT_WINDOW = 3
PAGINATION_DEFAULT_ORPHANS = 1

DEFAULT_MARKUP = 1 # Default Markup for threadedcomments (1=Markdown)
THREADEDCOMMENTS_BLOCKED_USERNAMES = (
    'wow',
    'gold',
)
