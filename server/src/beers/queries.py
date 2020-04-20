import db


def create_table():
    """ Create tables in the PostgreSQL database"""
    query = """
        CREATE TABLE IF NOT EXISTS beers (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            graduation NUMERIC(2, 1) NOT NULL
        )
        """
    db.insert(query)


def fetch(beer_id=None):
    """ Fetch data from PostgreSQL database"""
    if beer_id is not None:
        sql = "SELECT * FROM beers WHERE id=%s" % beer_id
        return db.fetch(sql, True)
    else:
        sql = "SELECT * FROM beers"
        return db.fetch(sql)


def insert(values):
    """ Insert data from PostgreSQL database"""
    sql = "INSERT INTO beers VALUES(%s);"
    return db.insert(sql, values)
