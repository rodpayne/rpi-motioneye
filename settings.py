
import logging
import os.path
import sys


PROJECT_PATH = os.path.dirname(sys.argv[0])

DEBUG = True
LOG_LEVEL = logging.DEBUG

TEMPLATE_PATH = os.path.join(PROJECT_PATH, 'templates')

STATIC_PATH = os.path.join(PROJECT_PATH, 'static')
STATIC_URL = '/static/'

LISTEN = '0.0.0.0'
PORT = 8765