# -*- encoding: UTF-8 -*-

#
#    Copyright 2013-2015
#
#      Rayco Abad-Martín <rayco.abad@gmail.com>
#      http://www.linkedin.com/in/rabad
#
#    This file is part of patrimonioULL.
#
#    patrimonioULL is free software: you can redistribute it and/or
#    modify it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    patrimonioULL is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with patrimonioULL.  If not, see
#    <http://www.gnu.org/licenses/>.
#

import os

# ******************************* PATHS *************************************
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))
STATIC_ROOT = os.path.join(BASE_DIR, 'collected_static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
LOG_ROOT = PROJECT_ROOT
# ******************************* PATHS *************************************

# ******************************* URLS **************************************
SITE_URL = '/patrimonioarte/'
STATIC_URL = '{SITE_URL}static/'.format(**locals())
MEDIA_URL = '{SITE_URL}media/'.format(**locals())
# ******************************* URLS **************************************

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'y6m(pfx#t*s+=6zb_3!0n&m)gios^8d)kv0@90x2)h7r1-hhr1'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATE_DEBUG = True

INTERNAL_IPS = ('127.0.0.1', )
ALLOWED_HOSTS = ['*']

# ******************************* ADMINS *************************************
ADMINS = (
    ('Rayco Abad-Martín', 'rabadmar@ull.edu.es'),
)
MANAGERS = ADMINS
# ******************************* ADMINS *************************************

# ******************************* LANGUAGE ***********************************
USE_I18N = True
USE_L10N = True
LANGUAGE_CODE = 'es'
TIME_ZONE = 'Atlantic/Canary'
USE_TZ = True
# ******************************* LANGUAGE ***********************************

# ******************************* INSTALLED APPS *****************************
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'core.apps.CoreConfig',
    'patrimonio.apps.PatrimonioConfig',
    'logentry_admin',
    'tinymce',
    'django_object_actions',
)
# ******************************* INSTALLED APPS *****************************

# ******************************* MIDDLEWARES ********************************
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)
# ******************************* MIDDLEWARES ********************************

# ************************* AUTHENTICATION CAS - ULL *************************
AUTHENTICATION_BACKENDS = (
    'core.backends.CASBackend',
)

CAS_SERVER_URL = 'https://loginpruebas.ull.es/cas-1/'
CAS_VERSION = 'CAS_2_SAML_1_0'
CAS_ADMIN_PREFIX = 'admin'
CAS_EXTRA_LOGIN_PARAMS = ''
CAS_IGNORE_REFERER = False
CAS_LOGOUT_COMPLETELY = True
CAS_REDIRECT_URL = SITE_URL
CAS_RETRY_LOGIN = True
CAS_TIPO_CUENTA_NOAUT = ['colectivo', ]
CAS_USERNAME_ATTRIBUTE = 'username'
LOGIN_URL = 'login'
LOGOUT_URL = 'logout'
# ************************* AUTHENTICATION CAS - ULL *************************

ROOT_URLCONF = 'patrimonioULL.urls'

WSGI_APPLICATION = 'patrimonioULL.wsgi.application'

# ******************************* DATABASES **********************************
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'name',
        'USER': 'user',
        'PASSWORD': 'password',
        'HOST': '',
        'PORT': '',
    },
}
# ******************************* DATABASES **********************************

# ******************************* TEMPLATES **********************************
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
# ******************************* TEMPLATES **********************************

# ******************************* EMAIL **************************************
import socket
EMAIL_SUBJECT_PREFIX = "patrimonioULL@" + socket.gethostname() + ": "
SERVER_EMAIL = "patrimonioULL@" + socket.getfqdn(socket.gethostname())

# ******************************* EMAIL **************************************

MAX_THUMB_SIZE = 100
MAX_IMAGEN_SIZE = 400

# FIXME: Migrate to patrimonio.settings
TIPOS_ESTADO = (
    ('Bueno', 'Bueno'),
    ('Malo', 'Malo'),
    ('Regular', 'Regular'),
)

# ************************* GOOGLE ANALYTICS *************************
INSTALLED_APPS += ('ganalytics', )
GANALYTICS_TRACKING_CODE = ''
TEMPLATES[0]['DIRS'] += ['templates']

# ************************* GOOGLE ANALYTICS *************************

# ******************************* SETTINGS LOCAL *****************************
try:
    SETTINGS_LOCAL
except NameError:
    try:
        from settings_local import *
    except ImportError:
        pass
# ******************************* SETTINGS LOCAL *****************************

# ******************************* LOGGING ************************************
LOG_FILENAME = os.path.join(LOG_ROOT, 'patrimonioULL.log')
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '[%(levelname)s] %(asctime)s <%(pathname)s>: %(message)s',
            'datefmt': '%d-%m-%Y %H:%M:%S',
        },
        'simple': {
            'format': '[%(levelname)s] %(asctime)s: %(message)s',
            'datefmt': '%d-%m-%Y %H:%M:%S',
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        }
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'filters': ['require_debug_false'],
            'include_html': True,
        },
        'default': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': LOG_FILENAME,
            'maxBytes': 5 * 1024 * 1024,  # 5MB
            'backupCount': 5,
            'formatter': 'simple',
        },
        'request_handler': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': LOG_FILENAME,
            'maxBytes': 5 * 1024 * 1024,  # 5MB
            'backupCount': 5,
            'formatter': 'simple',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['request_handler', 'mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
        'default': {
            'handlers': ['default', 'mail_admins'],
            'level': 'DEBUG',
            'propagate': True,
        },
    }
}
# ******************************* LOGGING ************************************
