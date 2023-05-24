import pymysql

class DatabaseConnection:
    def __init__(self):
        # Establish a connection to the MySQL database
        self.connection = pymysql.connect(host='localhost', user='root', password='qwerty', db='sys')
        self.cursor = self.connection.cursor()

    def insert_data(self, name, age):
        try:
            # Create the table if it doesn't exist
            create_table_query = """
                    CREATE TABLE IF NOT EXISTS student (
                          id INT AUTO_INCREMENT PRIMARY KEY,
                          name VARCHAR(50),
                          age INT
                    )
                """
            self.cursor.execute(create_table_query)
            print("Table created successfully")

            # Insert data into the table
            select_query = "SELECT * FROM student WHERE name = %s AND age = %s"
            self.cursor.execute(select_query, (name, age))
            existing_data = self.cursor.fetchone()

            if existing_data:
                print("Data already exists:", existing_data)
            else:
                # Insert data into the table
                insert_query = "INSERT INTO student (name, age) VALUES (%s, %s)"
                self.cursor.execute(insert_query, (name, age))
                self.connection.commit()
                print("Data inserted successfully")
        except pymysql.Error as e:
            print("Error occurred while connecting to MySQL:", e)

    def retrieve_data(self):
        try:
            # Retrieve all data from the table
            select_query = "SELECT * FROM student"
            self.cursor.execute(select_query)
            rows = self.cursor.fetchall()

            # Process the retrieved data
            for row in rows:
                print(row)
        except pymysql.Error as e:
            print("Error occurred while connecting to MySQL:", e)

    def close_connection(self):
        # Close the database connection
        if self.connection is not None:
            self.connection.close()


# Create an instance of the DatabaseConnection class
db = DatabaseConnection()

# Call the insert_data method to insert data into the table
db.insert_data('arun', 23)
db.insert_data('arun', 23)

# Call the retrieve_data method to retrieve data from the table
db.retrieve_data()

# Close the database connection
db.close_connection()
