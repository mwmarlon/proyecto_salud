from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []
    

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'proyectosalud',
        'USER': 'root1',
        'PASSWORD': '1234',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR.child('static')]

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.child('media')

#mail _settings
EMAIL_USE_TLS=True
EMAIL_HOST='smtp.gmail.com'
EMAIL_HOST_USER='mwmarlondavid@gmail.com'
EMAIL_HOST_PASSWORD='mwmd52128_'
EMAIL_PORT=587

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
