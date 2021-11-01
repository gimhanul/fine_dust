import pymysql
import time

class Database:
    def __init__(self):
        self.db = pymysql.connect(host='localhost', user = 'ubuntu', password = 'qlqjs',db = 'test')
        self.cur = self.db.cursor()
        print("nice!")

    def insertJson(self,finddust):
        tm = time.localtime()
        timedate ="{}-{}-{}_{}:{}".format(tm.tm_year,tm.tm_mon,tm.tm_mday,tm.tm_hour,tm.tm_min)
        sql="INSERT INTO dust(data) values(%s);"
        val=('{{"time":"{}", "find-dust":"{}"}}'.format(timedate,finddust))
        self.cur.execute(sql,val)
        self.db.commit()
        return "nice!"