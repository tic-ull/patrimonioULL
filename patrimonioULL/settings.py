# -*- encoding: UTF-8 -*-

import os

# ******************************* PATHS *************************************
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# ******************************* PATHS *************************************

# ******************************* URLS **************************************
STATIC_URL = '/patrimonioarte/static/'
MEDIA_URL = '/patrimonioarte/media/'
# ******************************* URLS **************************************

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'y6m(pfx#t*s+=6zb_3!0n&m)gios^8d)kv0@90x2)h7r1-hhr1'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATE_DEBUG = DEBUG

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
    'patrimonio',
    'logentry_admin',
    'tinymce',
)
# ******************************* INSTALLED APPS *****************************

# ******************************* MIDDLEWARES ********************************
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'django_cas.middleware.CASMiddleware',
)
# ******************************* MIDDLEWARES ********************************

AUTHENTICATION_BACKENDS = (
    'django_cas.backends.CASBackend',
)

# ************************* AUTHENTICATION CAS - ULL *************************
CAS_SERVER_URL = 'https://loginpruebas.ull.es/cas-1/'
CAS_VERSION = 'CAS_2_SAML_1_0'
# ************************* AUTHENTICATION CAS - ULL *************************

ROOT_URLCONF = 'patrimonioULL.urls'

WSGI_APPLICATION = 'patrimonioULL.wsgi.application'

# ******************************* DATABASES **********************************
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
# ******************************* DATABASES **********************************

MAX_THUMB_SIZE = 100
MAX_IMAGEN_SIZE = 400

# FIXME: Migrate to patrimonio.settings
TIPOS_ESTADO = (
    ('Bueno', 'Bueno'),
    ('Malo', 'Malo'),
    ('Regular', 'Regular'),
)

# ************************* SETTINGS LOCAL ***********************************
try:
    SETTINGS_LOCAL
except NameError:
    try:
        from settings_local import *
    except ImportError:
        pass
# ************************* SETTINGS LOCAL ***********************************
