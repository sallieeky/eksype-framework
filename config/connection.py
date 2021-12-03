import pymysql
import env


def connect():
    db = pymysql.connect(host=env.db_host, user=env.db_user,
                         passwd=env.db_pass, db=env.db_name)
    cursor = db.cursor()
    return db, cursor
