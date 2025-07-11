"""
Django settings for property_management project.

Generated by 'django-admin startproject' using Django 5.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.2/ref/settings/
"""
from django.core.files.storage import default_storage
from pathlib import Path
import os
# Load env
from dotenv import load_dotenv
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(BASE_DIR / '.env')


# SECURITY
SECRET_KEY   = os.getenv('SECRET_KEY')
DEBUG        = os.getenv('DEBUG', 'False') == 'True'
ALLOWED_HOSTS= os.getenv('ALLOWED_HOSTS', '').split(',')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'django-insecure-9rwz4h*-k2g4t(bdvzi1ojnntqmi@20a+9t=hvi8=g*wn5!=#u'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'properties',
    'tenants',
    'storages',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'property_management.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'property_management.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

# PostgreSQL via env



DATABASES = {
    'default': dj_database_url.config(conn_max_age=600, ssl_require=True)
}
# DATABASES = {
#     'default': {
#         'ENGINE'  : 'django.db.backends.postgresql',
#         'NAME'    : os.getenv('POSTGRES_DB'),
#         'USER'    : os.getenv('POSTGRES_USER'),
#         'PASSWORD': os.getenv('POSTGRES_PASSWORD'),
#         'HOST'    : os.getenv('POSTGRES_HOST'),
#         'PORT'    : os.getenv('POSTGRES_PORT'),
#     }
# }

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# At the top, after imports:
AWS_LOCATION = 'media'
STATICFILES_LOCATION = 'static'

# 1. Specify STATIC_URL and STATIC_ROOT
STATIC_URL  = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

# 2. AWS / DO Spaces configuration
AWS_ACCESS_KEY_ID       = os.getenv("DO_SPACES_KEY")
AWS_SECRET_ACCESS_KEY   = os.getenv("DO_SPACES_SECRET")
AWS_STORAGE_BUCKET_NAME = os.getenv("AWS_STORAGE_BUCKET_NAME")
AWS_S3_ENDPOINT_URL     = os.getenv("DO_SPACES_ENDPOINT")
AWS_S3_REGION_NAME      = os.getenv("DO_SPACES_REGION")

AWS_DEFAULT_ACL              = 'public-read'
AWS_QUERYSTRING_AUTH        = False
AWS_S3_OBJECT_PARAMETERS     = {"CacheControl": "max-age=86400"}
AWS_S3_CUSTOM_DOMAIN         = f"{AWS_STORAGE_BUCKET_NAME}.{AWS_S3_REGION_NAME}.digitaloceanspaces.com"

# 3. Define STORAGES with both default and staticfiles backends
STORAGES = {
    "default": {
        "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
        "OPTIONS": {
            "location": AWS_LOCATION,
        },
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

# 4. Media and static URLs pointing to Spaces
MEDIA_URL  = f"https://{AWS_S3_CUSTOM_DOMAIN}/{AWS_LOCATION}/"


