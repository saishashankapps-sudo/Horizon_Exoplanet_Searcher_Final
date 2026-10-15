import mysql.connector
from mysql.connector import Error

from config import DB_CONFIG
from logger import log_error


def create_connection():
    """Create and return a MySQL connection."""
    try:
        connection = mysql.connector.connect(**DB_CONFIG)

        if connection.is_connected():
            return connection

        log_error("MySQL connection was not established.")
        return None

    except Error as error:
        log_error(f"MySQL connection error: {error}")
        print(f"MySQL connection error: {error}")
        return None
