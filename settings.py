# -*- coding: utf-8 -*-

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
	('Víctor Muñoz', 'victorm@marshland.es'),
)
MANAGERS = ADMINS

DATABASES = {
	'default': {
		'ENGINE':   'django.db.backends.postgresql_psycopg2',
		'NAME':     'browner',
		'USER':     'browner',
		'PASSWORD': 'browner',
		'HOST':     '',
		'PORT':     '',
	}
}

TIME_ZONE = ''
LANGUAGE_CODE = 'es-es'
USE_I18N = False
USE_L10N = False

ADMIN_MEDIA_PREFIX = '/static/admin/'

SECRET_KEY = 'l3pb4d*&m1-5x!h2y!$j7*hwxmp9b$=t$3w5a2^2g+o%%!ygm0'

TEMPLATE_LOADERS = (
	'django.template.loaders.filesystem.Loader',
	'django.template.loaders.app_directories.Loader',
)
TEMPLATE_DIRS = (
	'/home/victorm/code/tasklist/browner/templates',
)

MIDDLEWARE_CLASSES = (
	'django.middleware.common.CommonMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
)


INSTALLED_APPS = (
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.admin',
	'django.contrib.staticfiles',
	'browner.dispatcher',
)

ROOT_URLCONF = 'browner.urls'
APPEND_SLASH = True

LOGIN_URL = '/login';
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

STATIC_URL = '/static/'
STATICFILES_DIRS = (
	'/home/victorm/code/tasklist/browner/static',
)

