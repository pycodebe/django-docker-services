from os import environ
from .common import *

DEBUG = False

SECRET_KEY = environ['SECRET_KEY']

ALLOWED_HOSTS = ['localhost', '127.0.0.1',]