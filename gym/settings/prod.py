from gym.settings.common import *
import pymysql

pymysql.install_as_MySQLdb()
import MySQLdb
import os

SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG = os.environ.get('DEBUG')
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '*').split(',')

# mysql db
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ["DB_NAME"],
        'USER': os.environ["DB_USERNAME"],
        'PASSWORD': os.environ["DB_PASSWORD"],
        'HOST': os.environ["DB_HOST"],
        'PORT': os.environ["DB_PORT"],
        'OPTIONS': {
            'init_command': 'SET sql_mode="STRICT_TRANS_TABLES"'
        }
    }
}
# 캐시 설정 redis
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": [(os.environ.get('REDIS_HOST', '127.0.0.1')), 6379],
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

# 디버깅
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'ERROR',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'ERROR',
        },
    },
}

CELERY_BROKER_URL = 'redis://redis:6379'
CELERY_RESULT_BACKEND = 'redis://redis:6379'
