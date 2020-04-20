import psycopg2
import connection


def beers():
    """ create tables in the PostgreSQL database"""
    query = """
        CREATE TABLE IF NOT EXISTS beers (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            graduation NUMERIC(2, 1) NOT NULL
        )
        """
    connection.connect(query)
