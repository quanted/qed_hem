"""
Django settings for QED project when running with Docker.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

from settings import *
import os
import socket
import sys

print('settings_docker.py')

# Get machine IP address
MACHINE_ID = socket.gethostname()

# Define ENVIRONMENTAL VARIABLES for project (replaces the app.yaml)
os.environ.update({
    'REST_SERVER_8': 'http://172.20.100.18',
    'PROJECT_PATH': PROJECT_ROOT,
    'SITE_SKIN': 'EPA',                          # Leave empty ('') for default skin, 'EPA' for EPA skin
    'CONTACT_URL': 'https://www.epa.gov/research/forms/contact-us-about-epa-research',

    # cts_api addition:
    'CTS_EPI_SERVER': 'http://172.20.100.18',
    'CTS_EFS_SERVER': 'http://172.20.100.12',
    'CTS_JCHEM_SERVER': 'http://172.20.100.12',
    'CTS_SPARC_SERVER': 'http://204.46.160.69:8080',
    'CTS_TEST_SERVER': 'http://172.20.100.16:8080',
    # 'CTS_VERSION': '1.8'  # Now set at settings.py
})

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = False
DEBUG = False
TEMPLATE_DEBUG = False



if not os.environ.get('UBERTOOL_REST_SERVER'):
    os.environ.update({'UBERTOOL_REST_SERVER': 'http://qed_nginx:7777'})  # Docker network
    print("REST backend = http://qed_nginx:7777")

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/
    
# SECURITY WARNING: keep the secret key used in production secret!
try:
#    SECRET_KEY= os.environ.get('DOCKER_SECRET_KEY')
    with open('secret_key_django_dropbox.txt') as f:
        SECRET_KEY = f.read().strip()
except:
    print "Secret file not set as env variable"
    #SECRET_KEY = 'Shhhhhhhhhhhhhhh'

try:
    HOSTNAME= os.environ.get('DOCKER_HOSTNAME')
#    with open('secret_key_django_dropbox.txt') as f:
#        SECRET_KEY = f.read().strip()
except:
    print "HOSTNAME address not set as env variable"
    HOSTNAME = 'unknown'

#try:
#    with open('my_ip_address.txt') as f:
#	IP_ADDRESS = f.read().strip()
#except IOError as e:
#    print "No IP address given"
#    IP_ADDRESS = '0.0.0.0'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = []
if HOSTNAME == "ord-uber-vm001":
    ALLOWED_HOSTS.append('134.67.114.1')
    ALLOWED_HOSTS.append('qedinternal.epa.gov')
    IS_PUBLIC = False
elif HOSTNAME == "ord-uber-vm003":
    ALLOWED_HOSTS.append('134.67.114.3')
    ALLOWED_HOSTS.append('qed.epa.gov')
    IS_PUBLIC = True
else:
    ALLOWED_HOSTS.append('192.168.99.100')  # Docker Machine IP (generally, when using VirtualBox VM)
    #ALLOWED_HOSTS.append('134.67.114.3')    # CGI NAT address (mapped to 'qed.epa.gov')
    ALLOWED_HOSTS.append('134.67.114.1')
    ALLOWED_HOSTS.append('qedinternal.epa.gov')
    #ALLOWED_HOSTS.append('qed.epa.gov')
    IS_PUBLIC = False

print("MACHINE_ID = {}").format(MACHINE_ID)
print("HOSTNAME = {}").format(HOSTNAME)
print("IS_PUBLIC = {}").format(IS_PUBLIC)

# Disable this because Django wants to email errors and there is no email server set up
# ADMINS = (
#     ('Ubertool Dev Team', 'ubertool-dev@googlegroups.com')
# )


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    # 'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'urls'

WSGI_APPLICATION = 'wsgi_docker.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

# Authentication
AUTH = True
LOGIN_URL = '/ubertool/login'
SESSION_EXPIRE_AT_BROWSER_CLOSE = True



# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/New_York'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_ROOT = '/src/collected_static/'

# Log to console in Debug mode
if DEBUG:
    import logging
    logging.basicConfig(
        level = logging.DEBUG,
        format = '%(asctime)s %(levelname)s %(message)s',
    )
