from mysite.settings import *

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-v-#0e6(@123=kkn-ctw$*&#ib3q4vcqpzl5+t23p8xtfrkyi!_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

#INSTALLED_APPS += ['compressor']

ALLOWED_HOSTS = ["127.0.0.1","https://dgango-travel.liara.run/", "dgango-travel.liara.run","www.django-travel.liara.run"]

# sites framework
SITE_ID = 2

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': dj_database_url.config(default='sqlite:///dummy.db')
}


STATIC_ROOT=BASE_DIR/'staticfiles'
MEDIA_ROOT=BASE_DIR/'media'

STATICFILES_DIRS = [
    BASE_DIR / 'static',
]


STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
]

# compressor
COMPRESS_ENABLED = True
COMPRESS_OFFLINE = True  