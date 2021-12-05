import pymysql
import config

db, cursor = config.connect(pymysql.cursors.DictCursor)


class DB:
    def __init__(self):
        pass

    def queryMany(self, query):
        cursor.execute(query)
        return cursor.fetchall()

    def queryOnly(self, query):
        cursor.execute(query)
        return cursor.fetchone()
