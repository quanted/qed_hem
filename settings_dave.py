"""
Django settings for QED project when developing.

NOTE: Make sure PyCharm django config is pointing to settings_local.py
instead of settings.py

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

from settings import *
import os
import sys

print('settings_dave.py')

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
#BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
TEMPLATE_ROOT = os.path.join(PROJECT_ROOT, 'templates_qed') #.replace('\\','/'))
os.path.join(PROJECT_ROOT, 'templates_qed')

# Get machine IP address
MACHINE_ID = "developer"

# CTS- Boolean for if it's on Nick's local machine or not..
NICK_LOCAL = False

# Define ENVIRONMENTAL VARIABLES
os.environ.update({
    'REST_SERVER_8': 'http://134.67.114.8',  # 'http://localhost:64399'
    'PROJECT_PATH': PROJECT_ROOT,
    'SITE_SKIN': 'EPA',                          # Leave empty ('') for default skin, 'EPA' for EPA skin
    'CONTACT_URL': 'https://www.epa.gov/research/forms/contact-us-about-epa-research',

    'CTS_TEST_SERVER': 'http://134.67.114.6:8080',
    'CTS_EPI_SERVER': 'http://134.67.114.8',
    'CTS_JCHEM_SERVER': 'http://134.67.114.2',
    'CTS_EFS_SERVER': 'http://134.67.114.2',
    'CTS_SPARC_SERVER': 'http://204.46.160.69:8080',
    # 'CTS_VERSION': '1.8'  # now set at settings.py
})

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = False
DEBUG = True
TEMPLATE_DEBUG = False

if not os.environ.get('UBERTOOL_REST_SERVER'):
    os.environ.update({'UBERTOOL_REST_SERVER': 'http://localhost:7777'})  # Local REST server
    print("REST backend = http://localhost:7777")

    # SECURITY WARNING: we keep the secret key in a shared dropbox directory
try:
    with open('secret_key_django_dropbox.txt') as f:
        SECRET_KEY = f.read().strip()
except IOError as e:
    print("Could not find secret file")  # for python 3x
    SECRET_KEY = 'Shhhhhhhhhhhhhhh'

    ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    'testserver',
]

#IS_PUBLIC = True
IS_PUBLIC = False

WSGI_APPLICATION = 'wsgi_local.application'

# Authentication
AUTH = False
LOGIN_URL = '/ubertool/login'
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

# Log to console in Debug mode
if DEBUG:
    import logging
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s %(levelname)s %(message)s',
    )
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_ROOT = (
	os.path.join(PROJECT_ROOT, 'hem_app\\static')
)

STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, "static_qed"),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

STATIC_URL = '/static_qed/'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dev_qed_dave',
        'USER': 'app_hem',
        'PASSWORD': 'Iw2c4L@bm0r',
        'HOST': 'darwin.rtpnc.epa.gov',
        'PORT': '3306'
        #'ENGINE': 'django.db.backends.postgresql_psycopg2',
        #'NAME': 'prod_dashboard',
        #'USER': 'dave',
        #'PASSWORD': 'cigar200',
        #'HOST': 'dalton.epa.gov',
        #'PORT': '5432'
    },
    'hem_db': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dev_hem_dave',
        'USER': 'app_hem',
        'PASSWORD': 'Iw2c4L@bm0r',
        'HOST': 'darwin.rtpnc.epa.gov',
        'PORT': '3306'
        #'ENGINE': 'django.db.backends.postgresql_psycopg2',
        #'NAME': 'prod_hem_app',
        #'USER': 'dave',
        #'PASSWORD': 'cigar200',
        #'HOST': 'dalton.epa.gov',
        #'PORT': '5432'
    },
}


DATABASE_ROUTERS = {'routers.HemRouter'}
# Application definition

INSTALLED_APPS = (
    #'cts_api',
    #'cts_testing',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #'mod_wsgi.server',  # Only needed for mod_wsgi express (Python driver for Apache) e.g. on the production server
    # 'docs',
    # 'rest_framework_swagger',
    #'cts_app',  # cts django app
    #'cts_app.filters',  # cts filters for pchem table
    #'cts_app.cts_testing',
    #'cts_app.cts_api',
    'splash_app',
    'hem_app',
    'crispy_forms',
    'rest_framework',
    #'ubertool_app',
    #'hwbi_app',
)

CRISPY_TEMPLATE_PACK = 'bootstrap3'

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

# Setups databse-less test runner (Only needed for running test)#
# TEST_RUNNER = 'testing.DatabaselessTestRunner'
