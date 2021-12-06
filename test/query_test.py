from helper.db import DB


class QueryTest:
    def __init__(self):
        pass

    def test_1():
        query = DB.queryMany("SELECT * FROM user")
        print(query)
