import os
import sqlite3

def init_db():
    """
    Creates the database by setting up the user_details, product_details, and price_history tables.
    If the tables already exist, they won't be recreated.
    """
    current_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(current_dir, 'price_tracker.db')

    # Connecting to the SQLite database or creating the database file if it doesn't exist)
    conn = sqlite3.connect(db_path)
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
            url TEXT UNIQUE NOT NULL,
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
            price DECIMAL(10, 2) NOT NULL,
            FOREIGN KEY (product_id) REFERENCES product_details (product_id)  
        )
    ''')

    # Closing the connection and Committing
    conn.commit()
    cursor.close()
    conn.close()













