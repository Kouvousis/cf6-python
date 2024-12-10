import mysql.connector
from mysql.connector import Error

def create_connection(host_name, user_name, user_password):
    connection = None
    
    try:
        connection = mysql.connector.connect(
            host = host_name,
            user = user_name,
            password = user_password
        )
        print("Connection to MySQL DB was successful")
    except Error as e:
        print(f"Error: {e}")
    return connection

def create_database(connection, query):
    cursor = connection.cursor()
    
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()

def main():
    conn = create_connection('localhost', '', '')
    
    if conn:
        create_database_query = "CREATE DATABASE codingcf6python"
        create_database(conn, create_database_query)
        conn.close()
        print("MySQL connection closed")
        

if __name__ == "__main__":
    main()
        