# Context Managers
# Context managers are a powerful feature in Python that helps you manage resources properly. 
# They ensure that resources are properly acquired and released, even if an error occurs. 
# The with statement is the most common way to use context managers.

"""
enter and exit
To create a context manager, you need to implement two magic methods:

__enter__: Called when entering the with block. It should return the resource to be managed.

__exit__: Called when exiting the with block, even if an exception occurs. It should handle cleanup.

The __exit__ method receives three arguments:

exc_type: The type of the exception (if any)

exc_val: The exception instance (if any)

exc_tb: The traceback (if any)
"""

# Practical Example: Database Connection Manager
# Let's create a context manager for database connections. This example shows how to properly manage database resources and handle transactions:

import sqlite3
import logging


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


class DatabaseConnection:
    def __init__(self, dbpath):
        self.dbpath = dbpath
        self.connection = None
        self.cursor = None
        
    def __enter__(self,):
        logging.info(f"Connecting to database: {self.dbpath}")
        self.connection = sqlite3.connect(self.dbpath)
        self.cursor = self.connection.cursor()
        return self.cursor
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            logging.error(f"An Error occured: {exc_val}")
            self.connection.rollback()
            logging.info("Transaction rollback")
            
        else:
            self.connection.commit()
            logging.info("Transaction commit")
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
            
        logging.info("Database connection closed.")
        
        """
        Python’s with statement checks the return value of __exit__. Here's how it works:
        - If __exit__ returns True, Python assumes you’ve handled the exception and it will suppress it (i.e., it won’t propagate outside the with block).
        - If __exit__ returns False (or None), Python will re-raise the exception after the context manager finishes, allowing it to be handled elsewhere or crash the program if unhandled.

        """
        
        # Return False to propagate exceptions, True to suppress them
        return False
        


try:
    # the DatabaseConnection(":memory:") :memory: is used to save in memory(ram) and when the program finish the database also finish
    with DatabaseConnection(":memory:") as cursor:
        
        cursor.execute("""
                       CREATE TABLE USERS (
                           id INTEGER PRIMARY KEY,
                           name TEXT,
                           email TEXT
                       )
                       """)
        
        #query data
        
        cursor.execute("SELECT * from users")
        print(cursor.fetchall())
        
        
        # Demonstrate transaction rollback on error
    with DatabaseConnection(":memory:") as cursor:
        cursor.execute("""
            CREATE TABLE users (
                id INTEGER PRIMARY KEY,
                name TEXT,
                email TEXT
            )
        """)
        cursor.execute(
            "INSERT INTO users (name, email) VALUES (?, ?)",
            ("Wewake", "contact@wewake.dev")
        )
        # cursor.execute("SELECT * FROM users")
        # rows = cursor.fetchone()
        # print(rows)
        
        # This will cause an error - table 'nonexistent' doesn't exist
        cursor.execute("SELECT * FROM nonexistent")
        
except sqlite3.OperationalError as e:
    print(f"Caught exception as:",e)
    