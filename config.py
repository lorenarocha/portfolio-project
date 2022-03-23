import os
from contact import email, senha

SECRET_KEY = 'lorena'

PROJECTS_PATH = os.path.dirname(os.path.realpath(__file__)) + '/static'
CV_PATH = os.path.dirname(os.path.realpath(__file__)) + '/static/cv'

MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = email
MAIL_PASSWORD = senha
