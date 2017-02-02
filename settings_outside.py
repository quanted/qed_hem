"""
Django settings for QED project when oustide EPA network.

This setup assumes everything is being hosted on
the local machine or a publicly-accessible server.

NOTE: CTS SPARC calculator still won't work, it's only accessible within
the EPA network.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

from settings import *
import os
import sys

print('settings_local.py')

# Get machine IP address
MACHINE_ID = "developer"



# Define ENVIRONMENTAL VARIABLES
os.environ.update({
    'REST_SERVER_8': 'http://localhost:64399',  # 'http://134.67.114.8'
    'PROJECT_PATH': PROJECT_ROOT,
    'SITE_SKIN': 'EPA',                          # Leave empty ('') for default skin, 'EPA' for EPA skin
    'CONTACT_URL': 'https://www.epa.gov/research/forms/contact-us-about-epa-research',

    # CTS additions #
    'CTS_EPI_SERVER': 'http://localhost:55342',  # port??
    'CTS_EFS_SERVER': 'http://ca-test-1.cloudapp.net',
    'CTS_JCHEM_SERVER': 'http://ca-test-1.cloudapp.net',
    'CTS_SPARC_SERVER': 'http://204.46.160.69:8080',
    'CTS_TEST_SERVER': '',
    # 'CTS_VERSION': '1.7'  # now at settings.py
})
DEBUG = True

NODEJS_HOST = 'localhost'
NODEJS_PORT = 4000

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
    print "Could not find secret file"
    SECRET_KEY = 'Shhhhhhhhhhhhhhh'

ALLOWED_HOSTS = [
	'localhost',
	'127.0.0.1'
]

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
        level = logging.DEBUG,
        format = '%(asctime)s %(levelname)s %(message)s',
    )