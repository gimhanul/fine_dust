import os
from pathlib import Path
import json

BASE_DIR = Path(__file__).resolve().parent
secret_file = os.path.join(BASE_DIR, 'secrets.json')

with open(secret_file) as f:
    secrets = json.loads(f.read())

def get_secret(setting, secrets=secrets):
    try:
        return secrets[setting]
    except KeyError:
        error_msg = "Set the {} environment variable".format(setting)
        return #raise ~~

class Config(object):
    CSRF_ENABLED = True
    SQLALCHEMY_ECHO = True #로그를 위한 플래그
    SQLALCHEMY_TRACK_MODIFICATIONS = False #수정사항 추적, 로그사용으로 불필요
    SECRET_KEY = get_secret("secret_key")
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://'+get_secret("DB_USER")+':'+get_secret("DB_PW")+'@'+get_secret("DB_HOST")+'/'+get_secret("DB_NAME")+'?charset=utf8'