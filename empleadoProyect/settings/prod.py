from .base import * #with the dot means that is located at the same subLevel on the carpet

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = []


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', #we changed to postgres instead of sqlite3
        'NAME': 'dbempleado',
        'USER': 'arturo',
        'PASSWORD': 'pitonpastel', #all this is neccesary if using postgres
        'HOST': 'localhost',
        'PORT': '5432',
    }
}



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR.child('static')]

#Para guardar archivos multimedia
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.child('media')