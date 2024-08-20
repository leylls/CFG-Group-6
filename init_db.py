import sqlite3

def init_db():
    """
    Creates the database by setting up the user_details, product_details, and price_history tables.
    If the tables already exist, they won't be recreated.
    """

    # Connecting to the SQLite database or creating the database file if it doesn't exist)
    conn = sqlite3.connect('price_tracker.db')
    cursor = conn.cursor()

    # Creating User Details Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user_details (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            username VARCHAR(100) NOT NULL,
            user_email VARCHAR(100),
            email_pref BOOLEAN DEFAULT 0  
        )
    ''')

    # Creating Product Details Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS product_details (
            product_id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_title VARCHAR(1000) NOT NULL,
            url TEXT NOT NULL,
            target_price DECIMAL(10, 2),
            email_notif BOOLEAN DEFAULT 0  
        )
    ''')

    # Creating Price History Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS price_history (
            log_id INTEGER PRIMARY KEY AUTOINCREMENT,  
            product_id INTEGER,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            currency VARCHAR(3),
            price REAL NOT NULL,
            FOREIGN KEY (product_id) REFERENCES product_details (product_id)  
        )
    ''')

    # Closing the connection and Committing
    conn.commit()
    cursor.close()
    conn.close()


# Example Use:
# from init_db import init_db

# init_db()












