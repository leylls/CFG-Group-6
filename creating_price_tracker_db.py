import sqlite3

# Connecting to Existing Database or Creating New One
conn = sqlite3.connect('price_tracker.db')
cursor = conn.cursor()

# Creating Users Table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        username VARCHAR(100) NOT NULL,
        email VARCHAR(100),
        email_pref BOOLEAN DEFAULT 0  
    )
''')

# Creating Products Table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        product_id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_title VARCHAR(1000) NOT NULL,
        target_price DECIMAL(10, 2),
        url TEXT NOT NULL,
        email_notification BOOLEAN DEFAULT 0  
    )
''')

# Creating Price History Table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS price_history (
        Log_id INTEGER PRIMARY KEY AUTOINCREMENT,  
        product_id INTEGER,
        price REAL NOT NULL,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
        currency VARCHAR(3),
        FOREIGN KEY (product_id) REFERENCES products (product_id)  
    )
''')

# Committing the Data Insertions and Closing the Connection to the Database
conn.commit()
cursor.close()
conn.close()








