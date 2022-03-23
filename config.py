import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = 'lorena'

PROJECTS_PATH = os.path.dirname(os.path.realpath(__file__)) + '/static'
CV_PATH = os.path.dirname(os.path.realpath(__file__)) + '/static/cv'

MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = os.getenv('EMAIL')
MAIL_PASSWORD = os.getenv('SENHA')
