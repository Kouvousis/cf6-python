import mysql.connector
from mysql.connector import Error

def create_connection(host_name, user_name, user_password, db_name, port):
    conn = None
    
    try:
        conn = mysql.connector.connect(
            host = host_name,
            user = user_name,
            password = user_password,
            database = db_name,
            port = port 
        )
        print("Connection to MySQL DB was successful")
    except Error as e:
        print(f"Error {e} occurred")
    return conn

def create_tables(conn):
    create_teachers_table = """
    CREATE TABLE IF NOT EXISTS teachers (
        id INTEGER PRIMARY KEY,
        firstname VARCHAR(50),
        lastname VARCHAR(50),
        age INTEGER
    )
    """
    
    create_students_table = """
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        firstname VARCHAR(50),
        lastname VARCHAR(50)
    )
    """
    
    cursor = conn.cursor()
    try:
        cursor.execute("BEGIN")
        cursor.execute(create_teachers_table)
        cursor.execute(create_students_table)
        conn.commit()
        print("Tables created successfully")
    except Error as e:
        print(f"Error {e} occurred")
        conn.rollback()
    finally:
        cursor.close()

def main():
    conn = create_connection('localhost', '', '', 'codingcf6python', '3306')
    if conn:
        create_tables(conn)
        conn.close()
        print("MySQL connection closed.")

if __name__ == "__main__":
    main()