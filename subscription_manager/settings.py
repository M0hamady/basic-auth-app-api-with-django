import os
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
from datetime import timedelta

SECRET_KEY = 'django-insecure-=s=#4*__j!##yu23zx2lxt*1m+csw6xs1s^t9@=r68u800c!)7'
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1','.vercel.app', '.now.sh']

INSTALLED_APPS = [
    'whitenoise.runserver_nostatic',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'authentication',
    'subscriptions',
    'services',
    'payments',
    'dashboard',
    'rest_framework',
    'corsheaders',  # CORS headers
    'rest_framework_simplejwt.token_blacklist',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # Added
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'subscription_manager.urls'

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
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',  # Keeps JWTAuthentication for all views
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',  # Require authentication for all views by default
    ),
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,  # Ensure this is set to True to blacklist old refresh tokens
}
WSGI_APPLICATION = 'subscription_manager.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'neondb',  # Database name from the new URL
        'USER': 'neondb_owner',  # User from the new URL
        'PASSWORD': 'VlYHKmWofG09',  # Password from the new URL
        'HOST': 'ep-wild-fog-a2k3qfnr-pooler.eu-central-1.aws.neon.tech',  # Host from the new URL
        'PORT': '5432',  # Port (default for PostgreSQL)
        'OPTIONS': {
            'sslmode': 'require',  # Forces SSL mode
        },
    }
}



AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files
STATIC_URL = '/static/'
# STATICFILES_DIRS = [BASE_DIR / 'static']
# STATIC_ROOT = BASE_DIR / 'staticfiles'
STATIC_ROOT = os.path.join(BASE_DIR ,'staticfiles')
STATIC_DIRS = [os.path.join(BASE_DIR ,'static')]

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = 'authentication.CustomUser'

# CORS settings
CORS_ALLOW_ALL_ORIGINS = True
FRONTEND_URL = 'https://react-secure-app-quick-start-qzexrcfi2-m0hamadys-projects.vercel.app/'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
SMTP_SERVER = 'smtp.titan.email'
SENDER_EMAIL = 'support@codeocean.tech'
EMAIL_PASSWORD = 'Mohammedy@258147369'  # Use environment variables for security
DEFAULT_FROM_EMAIL = 'support@codeocean.tech'


# sudo add-apt-repository universe
# sudo apt update
# sudo apt install python3-pip python3-dev
# pip3 install gunicorn

# gunicorn subscription_manager.wsgi:application
# gunicorn -b 0.0.0.0:8000 subscription_manager.wsgi:application
