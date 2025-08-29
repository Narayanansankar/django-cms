"""
Django settings for BlogProject project.

This file contains all the necessary configurations for the blog,
including app registration, database setup, custom settings for user
authentication, the CKEditor, and a robust static files setup for
both development and production.
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# Use the unique key that PyCharm/Django generated for your project.
SECRET_KEY = 'django-insecure-your-secret-key-goes-here'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    # Default Django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles', # Manages static files

    # Third-party apps
    'ckeditor',

    # My apps
    'blog',
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

# The root URL configuration file for the project.
# Make sure this matches your project folder name.
ROOT_URLCONF = 'BlogProject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # This tells Django where to find your project-level templates like 'base.html'.
        'DIRS': [BASE_DIR / 'templates'],
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

# Make sure this matches your project folder name.
WSGI_APPLICATION = 'BlogProject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

# This is the URL your templates will use to find the files (e.g., /static/css/styles.css)
STATIC_URL = 'static/'

# This tells Django's 'findstatic' command where to find your *source* static files.
# It should point to the 'static' folder you created at the project's root.
STATICFILES_DIRS = [
    BASE_DIR / "static",
]

# This is the single directory where `collectstatic` will dump all static files.
# It's only used for production deployment. Do not put your own files in here.
STATIC_ROOT = BASE_DIR / 'staticfiles'


# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# -------------------------------------------------------------------------- #
# ---               CUSTOM SETTINGS FOR OUR BLOG PROJECT                 --- #
# -------------------------------------------------------------------------- #

# Redirect users to the home page (blog list) after a successful login.
LOGIN_REDIRECT_URL = '/'

# Redirect users to the home page after a successful logout.
LOGOUT_REDIRECT_URL = '/'

# CKEditor (Rich Text Editor) Configuration
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'height': 300,
        'width': '100%',
    },
}