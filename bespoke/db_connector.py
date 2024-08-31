import os
import psycopg2
from psycopg2.extras import RealDictCursor

def get_db_connection():
    """
    Establishes and returns a connection to the PostgreSQL database.

    Returns:
        connection: The PostgreSQL database connection object.
    """
    try:
        connection = psycopg2.connect(
            dbname=os.getenv('DB_NAME'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            host=os.getenv('DB_HOST'),
            port=os.getenv('DB_PORT'),
            cursor_factory=RealDictCursor
        )
        return connection
    except Exception as error:
        print(f"Error connecting to the database: {error}")
        raise

def close_db_connection(connection):
    """
    Closes the given database connection.

    Args:
        connection: The database connection to close.
    """
    if connection:
        connection.close()
