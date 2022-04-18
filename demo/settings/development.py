import environ
from .common import *

env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, 'settings', 'development.env'))

DEBUG = True

SECRET_KEY = env('SECRET_KEY')

ALLOWED_HOSTS = ['127.0.0.1', 'localhost',]

if DEBUG:
    INSTALLED_APPS += ['debug_toolbar',]
    MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware',]
    INTERNAL_IPS = ['127.0.0.1',]