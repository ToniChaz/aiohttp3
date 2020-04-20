import psycopg2


def connect(query):
  """ Connect to the PostgreSQL database server """
  conn = None

  print("Connecting to the PostgreSQL database...")
  try:
    # Create connection
    conn = psycopg2.connect(
        database="aiohttp3_db",
        user="aiohttp3",
        password="1234",
        host="database",
        port="5432"
    )
    # Get the cursor
    cur = conn.cursor()
    # Execute the query
    print("Query executing: %s" % query)
    cur.execute(query)
    # Close communication with the PostgreSQL database server
    cur.close()
    # Commit the changes
    conn.commit()
  except (Exception, psycopg2.DatabaseError) as error:
    print(error)
  finally:
    if conn is not None:
      conn.close()
