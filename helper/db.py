import pymysql
import config

db, cursor = config.connect(pymysql.cursors.DictCursor)


class DB:
    def __init__(self):
        pass

    def queryMany(query):
        cursor.execute(query)
        return cursor.fetchall()

    def queryOnly(query):
        cursor.execute(query)
        return cursor.fetchone()
