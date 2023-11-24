# Importing the required libraires
import mysql.connector as mysql
from mysql.connector import Error as err
# Creating the class to have the database
class Database:
    def __init__(self):
        # Initialize instance variables
        self.err = err
        self.connection = None
        self.cursor = None

        # Connecting to the database
        try:
            self.connection = mysql.connect(
                host='localhost',
                user='root',
                password='new_password',
                database='accounts'
            )
            self.cursor = self.connection.cursor()

        except Exception as e:
            print(f"Error: {e}")
