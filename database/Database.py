import pymysql
import time
import os
from pathlib import Path
import json

BASE_DIR = Path(__file__).resolve().parent.parent
secret_file = os.path.join(BASE_DIR, 'secrets.json')

with open(secret_file) as f:
    secrets = json.loads(f.read())

def get_secret(setting, secrets=secrets):
    try:
        return secrets[setting]
    except KeyError:
        error_msg = "Set the {} environment variable".format(setting)
        return #raise ~~

class Database:
    def __init__(self):
        self.db = pymysql.connect(host=get_secret("DB_HOST"), user = get_secret("DB_USER"), password = get_secret("DB_PW"),db = get_secret("DB_NAME"))
        self.cur = self.db.cursor()
        print("nice!")

    #데이터 출력
    def selectAllJson(self):
        sql = "select * from dust;"
        self.cur.execute(sql)
        result = self.cur.fetchall()
        return result

    #시간 마다 미세먼지 측정 값
    def insertJson(self,finddust):
        tm = time.localtime()
        timedate ="{}-{}-{}_{}:{}".format(tm.tm_year,tm.tm_mon,tm.tm_mday,tm.tm_hour,tm.tm_min)
        sql="INSERT INTO dust(data) values(%s);"
        val=('{{"time":"{}", "find-dust":"{}"}}'.format(timedate,finddust))
        self.cur.execute(sql,val)
        self.db.commit()
        return "nice!"