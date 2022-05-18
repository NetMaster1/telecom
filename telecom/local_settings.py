# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-2e8+b%t857zlf8#31v^%$pbx!m2&&wnx++^92k28nf8vd0+i8i'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', 'www.rostelecom.org', 'rostelecom.org']

EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_POSRT = 537
EMAIL_HOST_USER = '79200711112@yandex.ru'
EMAIL_HOST_PASSWORD = 'unN-uWw-y7U-VLB'
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'requests_db',
        'USER': 'postgres',
        'PASSWORD': 'ylhio65v',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}