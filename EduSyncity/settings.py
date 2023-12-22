"""
Django settings for EduSyncity project.

Generated by 'django-admin startproject' using Django 2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'o9oxf@@)o0q=^55b$@sqz7zow(+dpehq@g3+zp7*9*c$skmaa5'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'sslserver',
    'corsheaders',
    'EduAdmin.apps.EduadminConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'EduCore',
    'EduExam',
]

MIDDLEWARE = [
    'django_cookies_samesite.middleware.CookiesSameSite',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
     'corsheaders.middleware.CorsMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'EduSyncity.urls'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  
CORS_ALLOWED_ORIGINS =['*']
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
ACCESS_CONTROL_ALLOW_ORIGIN = ['*']
SECURE_SSL_REDIRECT = True
DCS_SESSION_COOKIE_SAMESITE = 'None'
DCS_SESSION_COOKIE_SECURE = True
DCS_SESSION_COOKIE_HTTPONLY = False 


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

WSGI_APPLICATION = 'EduSyncity.wsgi.application'
AUTH_USER_MODEL = 'EduAdmin.User'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.mysql',
    #     'NAME': 'Edusyncity',
    #     'USER': 'harry',
    #     'PASSWORD':'Kiet@123',
    #     'HOST':'10.21.67.7',
    #     'PORT':'3306',
    # }
    #  'default': {
    #     'ENGINE': 'django.db.backends.mysql',
    #     'NAME': 'Edusyncity',
    #     'USER': 'harry',
    #     'PASSWORD':'Kiet@123',
    #     'HOST':'0.tcp.in.ngrok.io',
    #     'PORT':'18529',
    # }
     'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'Edusyncity',
        'USER': 'nikhil',
        'PASSWORD':'Nik212107@',
        'HOST':'localhost',
        'PORT':'3306',
    }

}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
