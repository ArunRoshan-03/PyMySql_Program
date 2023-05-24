import pymysql


class DatabaseConnection:

    def __init__(self, cursor):
        self.cursor = cursor

    def insert_data(self, name, age, table_name):
        try:
            create_table_query = f"""
                    CREATE TABLE IF NOT EXISTS {table_name} (
                          id INT AUTO_INCREMENT PRIMARY KEY,
                          name VARCHAR(50),
                          age INT
                    )
                """
            self.cursor.execute(create_table_query)
            print("Table created successfully")
            select_query = f"SELECT * FROM {table_name} WHERE name = %s AND age = %s"
            self.cursor.execute(select_query, (name, age))
            existing_data = self.cursor.fetchone()

            if existing_data:
                print("Data already exists:", existing_data)
            else:
                insert_query = f"INSERT INTO {table_name} (name, age) VALUES (%s, %s)"
                self.cursor.execute(insert_query, (name, age))
                self.cursor.connection.commit()
                print("Data inserted successfully")
        except pymysql.Error as e:
            print("Error occurred while connecting to MySQL:", e)

    def retrieve_data(self, table_name):
        try:
            select_query = f"SELECT * FROM {table_name}"
            self.cursor.execute(select_query)
            rows = self.cursor.fetchall()
            for row in rows:
                print(row)
        except pymysql.Error as e:
            print("Error occurred while connecting to MySQL:", e)
