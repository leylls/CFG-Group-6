# FOR TESTING BE WHILE FE IS BEING TESTED
# UNCOMMENT LINE 58 TO CREATE DB
# UNCOMMENT LINES 62 TO 89 TO POPULATE DB ONCE, COMMENT AGAIN SO ENTRIES ARE NOT DUPLICATED

import sqlite3

def init_db():
    """
    Creates the database by setting up the user_details, product_details, and price_history tables.
    If the tables already exist, they won't be recreated.
    """

    # Connecting to the SQLite database or creating the database file if it doesn't exist)
    conn = sqlite3.connect('back_end/price_tracker.db')
    cursor = conn.cursor()

    # Creating User Details Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user_details(
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            username VARCHAR(100) NOT NULL,
            user_email VARCHAR(100),
            email_pref BOOLEAN DEFAULT 0  
        )
    ''')

    # Creating Product Details Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS product_details(
            product_id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_title VARCHAR(1000) NOT NULL,
            url TEXT NOT NULL,
            target_price DECIMAL(10, 2),
            email_notif BOOLEAN DEFAULT 0  
        )
    ''')

    # Creating Price History Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS price_history(
            log_id INTEGER PRIMARY KEY AUTOINCREMENT,  
            product_id INTEGER,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            currency VARCHAR(3),
            price DECIMAL(10, 2),
            FOREIGN KEY (product_id) REFERENCES product_details (product_id)  
        )
    ''')

    # Closing the connection and Committing
    conn.commit()
    cursor.close()
    conn.close()


# EXAMPLE USE
# from init_db import init_db

# init_db()

# MOCK DATA FOR BE TESTING

# conn = sqlite3.connect('price_tracker.db')
# cur = conn.cursor()

# insert_user_query = '''INSERT INTO user_details(username, user_email, email_pref)
# VALUES ('Test_User', 'student@cfg.com', 1)'''

# cur.execute(insert_user_query)

# data = [('Wireless Earbuds', 'https://www.amazon.co.uk/Bluetooth-Headphones-Cancelling-Earphones-Waterproof-Black/dp/B0CHYV6312', 25.99, 1),
# ('Vacuum', 'https://www.amazon.co.uk/Shark-NZ801UKT-Lift-Away-Anti-Hair-Technology/dp/B07WQH7TJ4', 175, 1),
# ('Oral-B Toothbrush', 'https://www.amazon.co.uk/Oral-B-Toothbrushes-Christmas-Toothbrush-Whitening/dp/B0C14428DR', 98, 1)]

# cur.executemany('''
#                 INSERT INTO product_details(product_title,url,target_price,email_notif)
#                 VALUES (?, ?, ?, ?)''', data)

# data2 = [(1,'2024-08-19 02:56','£','30.99'),
#          (2,'2024-08-19 02:56','£','190.99'),
#          (3,'2024-08-19 02:56','£','115.99')]

# cur.executemany('''
#                  INSERT INTO price_history(product_id,timestamp,currency,price )
#                  VALUES (?, ?, ?, ?)''', data2)


# conn.commit()
# cur.close()
# conn.close()

# VISUALIZE TABLES
def display_table(table_name):
    conn = sqlite3.connect('back_end/price_tracker.db')
    cur= conn.cursor()
    cur.execute(f"SELECT * FROM {table_name}")
    rows = cur.fetchall()
    print(f"Contents of {table_name}:")
    for row in rows:
        print(row)
    print("\n")
    cur.close()
    conn.close()
    
display_table('user_details')
display_table('product_details')
display_table('price_history')
