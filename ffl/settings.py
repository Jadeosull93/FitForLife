"""
Django settings for ffl project.

Generated by 'django-admin startproject' using Django 3.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import dj_database_url
import os
import logging
import logging.config


LOGGING_CONFIG = None
logging.config.dictConfig({
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'console': {
            # exact format is not important, this is the minimum information
            'format': '%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'console',
        },
    },
    'loggers': {
    # root logger
        '': {
            'level': 'INFO',
            'handlers': ['console'],
        },
    },
})
# Get an instance of a logger
logger = logging.getLogger('django') #__name__ specifies the module name, django is the general purpose logger
# If we are building locally operate in development mode
# other wise turn off development
development = os.environ.get('DEVELOPMENT',"False") #we want to run in debug mode
heroku = os.environ.get('HEROKU',"False") # we are deploying on Heroku
heroku_postgres = os.environ.get('HEROKU_POSTGRES',"True") # Use a Heroku hosted database
use_test_database=os.environ.get('USE_TEST_DATABASE',"False")

#heroku = False
# SECURITY WARNING: don't run with debug turned on in production!
if development == 'True':
    DEBUG=True

# Build paths inside the project like this: BASE_DIR / 'subdir'.
#BASE_DIR = Path(__file__).resolve().parent.parent
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')    



#ALLOWED_HOSTS = ['django-ffl-app.herokuapp.com','127.0.0.1']
#if development == 'True':
#    ALLOWED_HOSTS = ['localhost','127.0.0.1']
#    logger.warn('using allowed Hosts for localhost because we are in development mode: ' + str(ALLOWED_HOSTS) + ' development ' + str(development))


if heroku == "True":
    heroku_postgres = "True"
    ALLOWED_HOSTS = [os.environ.get('HEROKU_HOSTNAME'),'localhost','127.0.0.1']
    logger.warn('using allowed Hosts for heroku and heroku database instance because we are in production mode:[' + str(ALLOWED_HOSTS) + ']')
else:
    ALLOWED_HOSTS = ['localhost','127.0.0.1']

# ALLOWED_HOSTS = ['localhost','django-ffl-app.herokuapp.com']
# Application definition
# 'allauth', #provides user registration, password reset etc
# 'allauth.account',
# 'allauth.socialaccount', #login via google, facebook etc
INSTALLED_APPS = [
    'products.apps.ProductsConfig',
    'plans.apps.PlansConfig',
    'workouts.apps.WorkoutsConfig',
    'planworkouts.apps.PlanWorkoutsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'home',	
    'cart',
    'crispy_forms',
    'storages'	
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

ROOT_URLCONF = 'ffl.urls'

CRISPY_TEMPLATE_PACK = 'bootstrap4'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
            os.path.join(BASE_DIR, 'templates', 'allauth'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request', # `allauth` needs this from django
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
                'cart.contexts.cart_contents',
            ],
	    #required by crispy forms  	
            'builtins': [
                'crispy_forms.templatetags.crispy_forms_tags',
                'crispy_forms.templatetags.crispy_forms_field',
            ]
        },
    },
]

MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
)

SITE_ID = 1

ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE = True
ACCOUNT_USERNAME_MIN_LENGTH = 4
LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/'

WSGI_APPLICATION = 'ffl.wsgi.application'

if heroku_postgres == 'True':
    logger.warn('heroku_postgres =' + str(heroku_postgres))
else:
    logger.warn('else heroku_postgres =' + str(heroku_postgres))


if 'DATABASE_URL' in os.environ:
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }
    logger.warn('using Heroku postresql database: to $DATABASE_URL ')
elif use_test_database == "True":
       DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    } 

else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'ffl_database', 
            'USER': 'djangouser', 
            'PASSWORD': 'djangouser90',
            'HOST': '127.0.0.1', 
            'PORT': '5432',
            }
    }
    logger.warn('using local database: ')


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-uk'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/
STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Stripe
FREE_DELIVERY_THRESHOLD = 50
STANDARD_DELIVERY_PERCENTAGE = 10

logger.warn('Settings completed: development : ' + str(development))
logger.warn('Settings completed: heroku : ' + str(heroku))
logger.warn('Settings completed: heroku database: ' + str(heroku_postgres))
logger.warn('Settings completed: allowed hosts: ' + str(ALLOWED_HOSTS))
logger.warn('Settings completed: STATICFILES_DIRS: ' + str(STATICFILES_DIRS))
logger.warn('Settings completed: MEDIA_ROOT: ' + str(MEDIA_ROOT))



