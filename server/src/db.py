import psycopg2


class DBConn:
    def __init__(self):
        self.conn = psycopg2.connect(
            database="aiohttp3_db",
            user="aiohttp3",
            password="1234",
            host="database",
            port="5432"
        )
        self.cur = self.conn.cursor()

    def cursor(self):
        return self.cur

    def close(self):
        self.cur.close()
        self.conn.close()


def insert(sql, values=None):
    """ Execute query in PostgreSQL database server """
    db = None

    try:
        db = DBConn()
        cursor = db.cursor()
        if values is not None:
            cursor.execute(sql)
        elif type(values) is list:
            cursor.executemany(sql, values)
        else:
            cursor.execute(sql, (values,))
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if db is not None:
            db.close()


def fetch(sql, one=False):
    """ Insert in PostgreSQL database server """
    db = None

    try:
        db = DBConn()
        cursor = db.cursor()
        if one:
            cursor.execute(sql)
            return cursor.fetchone()
        else:
            cursor.execute(sql)
            return cursor.fetchall()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if db is not None:
            db.close()
