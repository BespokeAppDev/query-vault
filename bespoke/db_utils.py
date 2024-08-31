import psycopg2
from psycopg2.extras import Json
from db_connector import get_db_connection, close_db_connection

def save_log_to_db(log_entry):
    """
    Saves a log entry to the PostgreSQL database.

    Args:
        log_entry (dict): The log entry to save.
    """
    connection = None
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        insert_query = """
        INSERT INTO logs (id, log_data)
        VALUES (%s, %s)
        """
        cursor.execute(insert_query, (log_entry['id'], Json(log_entry)))
        connection.commit()
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error saving log to database: {error}")
    finally:
        close_db_connection(connection)

def retrieve_logs(user_id=None):
    """
    Retrieves logs from the PostgreSQL database, optionally filtered by user ID.

    Args:
        user_id (str, optional): The ID of the user whose logs to retrieve.

    Returns:
        list: A list of log entries retrieved from the database.
    """
    connection = None
    logs = []
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        if user_id:
            select_query = "SELECT log_data FROM logs WHERE log_data->>'user_id' = %s"
            cursor.execute(select_query, (user_id,))
        else:
            select_query = "SELECT log_data FROM logs"
            cursor.execute(select_query)
        logs = cursor.fetchall()
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error retrieving logs from database: {error}")
    finally:
        close_db_connection(connection)
    return [log['log_data'] for log in logs]
