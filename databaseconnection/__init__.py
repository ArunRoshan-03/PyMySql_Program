import pymysql

try:
    # Establish a connection to the MySQL database
    connection = pymysql.connect(host='localhost', user='root', password='qwerty', db='sys')

    # Check if the connection was successful
    if connection is not None:
        print("Connection established successfully")

        # Create a cursor object
        cursor = connection.cursor()

        # Create the table if it doesn't exist
        create_table_query = """
                    CREATE TABLE IF NOT EXISTS m_table (
                          id INT PRIMARY KEY,
                          name VARCHAR(50),
                          age INT
                    )
                """
        cursor.execute(create_table_query)
        print("Table created successfully")

        # Insert data into the table
        sql = "INSERT INTO m_table (name, age) VALUES (%s, %s)"
        values = ('Arun', 34)

        cursor.execute(sql, values)

        # Commit the changes to the database
        connection.commit()

        print("Data inserted successfully")

    else:
        print("Connection not established successfully")

except pymysql.Error as e:
    print("Error occurred while connecting to MySQL:", e)

finally:
    # Close the database connection
    if connection is not None:
        connection.close()
