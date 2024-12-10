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

def insert_teacher(connection, teacher):
    cursor = connection.cursor()
    
    try:
        cursor.execute(
            "INSERT INTO teachers (id, firstname, lastname, age) VALUES (%s, %s, %s, %s)",
            teacher
        )
        connection.commit()
        print("Teacher inserted successfully")
    except Error as e:
        print(f"Error {e} occurred")
        connection.rollback()
    finally:
        cursor.close()



def main():
    conn = create_connection('localhost', '', '', 'codingcf6python', '3306')
    
    if conn:
        teacher = (1, "John", "Doe", 33)
        insert_teacher(conn, teacher)
        conn.close()
        print("MySQL connection closed")
        
    

if __name__ == "__main__":
    main()