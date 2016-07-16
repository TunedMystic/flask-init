import os


# Default settings for the application.

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))

BASE_DIR = os.path.dirname(PROJECT_DIR)

STATIC_DIR = os.path.join(PROJECT_DIR, 'static')

TEMPLATES_DIR = os.path.join(PROJECT_DIR, 'templates')

DEBUG = os.getenv('DEBUG', False) in ['True']

SECRET_KEY = os.getenv('SECRET_KEY', 'secret-key')

LOG_FILE = os.path.join(BASE_DIR, 'logs', 'app.log')


# Misc settings.

HOST = '0.0.0.0'

PORT = 8001


# Gunicorn settings.

bind = '{}:{}'.format(HOST, PORT)

accesslog = os.path.join(BASE_DIR, 'logs', 'gunicorn-access.log')

errorlog = os.path.join(BASE_DIR, 'logs', 'gunicorn-error.log')

reload = True
