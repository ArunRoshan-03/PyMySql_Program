import pymysql

try:
    # Establish a connection to the MySQL database
    connection = pymysql.connect(host='localhost', user='root', password='qwerty')

    # Check if the connection was successful
    if connection is not None:
        print("Connection established successfully")

        # Create a cursor object
        cursor = connection.cursor()

        # Execute a query to get the MySQL version
        cursor.execute("SELECT VERSION()")

        # Fetch the version from the result
        version = cursor.fetchone()[0]

        # Print the version
        print("MySQL version:", version)

    else:
        print("Connection not established successfully")
except pymysql.Error as e:
    print("Error occurred while connecting to MySQL:", e)
finally:
    # Close the database connection
    if connection is not None:
        connection.close()
