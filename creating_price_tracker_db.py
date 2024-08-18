import sqlite3

# Connecting to Existing Database or Creating New One
conn = sqlite3.connect('price_tracker.db')
cursor = conn.cursor()

# Creating Users Table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        username VARCHAR(100) NOT NULL,
        email VARCHAR(100) UNIQUE NOT NULL,
        email_pref BOOLEAN DEFAULT 0  
    )
''')

# Inserting Example User data into the Users Table
users = [
    (1, 'Shaira', 'shaira@CFGdegree.co.uk', 0),
    (2, 'Eva', 'eva@CFGdegree.co.uk', 0),
    (3, 'Violeta', 'violeta@CFGdegree.co.uk', 0),
    (4, 'Ikram', 'ikram@CFGdegree.co.uk', 0),
    (5, 'Leyla', 'leyla@CFGdegree.co.uk', 0)
]

sql_users = "INSERT INTO users (user_id, username, email, email_pref) VALUES (?, ?, ?, ?)"
cursor.executemany(sql_users, users)

# Creating Products Table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        product_id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_title VARCHAR(1000) NOT NULL,
        currency VARCHAR(3),
        current_price DECIMAL(10, 2),
        target_price DECIMAL(10, 2),  
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
        url TEXT NOT NULL,
        email_pref BOOLEAN DEFAULT 0  
    )
''')

# Inserting Example Products from Web Scraped data into the Products Table
products = [
    (1, 'Amazon Fire HD 10 Kids Pro tablet | ages 6–12, 10.1" brilliant screen, long battery life, parental controls, slim case, 2023 release, 32 GB, Happy Day', '£', '199.99', '150.00', '2024-08-08 19:26', 'https://www.amazon.co.uk/dp/B0BL6GJVZS', 0),  # Updated to include target_price and email_pref
    (2, 'It Ends With Us: The emotional #1 Sunday Times bestseller, Now a major film starring Blake Lively and Justin Baldoni (Lily & Atlas, 1)', '£', '5.00', '4.00', '2024-08-08 19:26', 'https://www.amazon.co.uk/Ends-Us-Colleen-Hoover/dp/1471156265/', 0),
    (3, 'Mighty Patch Hero Cosmetics Original Patch - Hydrocolloid Acne Pimple Patch for Covering Zits and Blemishes, Spot Stickers for Face and Skin (36 Count)', '$', '27.88', '20.00', '2024-08-08 19:26', 'https://www.amazon.com/Mighty-Patch-Hydrocolloid-Absorbing-count/dp/B074PVTPBW', 0),
    (4, 'HP S1 8GB RAM DDR4 (1x8GB) Laptop Ram 3200 MHz SODIMM PC4-2500 CL22 Memory 1.2v - 2E2M5AA#ABB', '$', '19.69', '15.00', '2024-08-08 19:26', 'https://www.amazon.com/HP-Single-3200MHz-Laptop-Memory/dp/B0948X9C9N/ref=sr_1_3?sr=8-3', 0)
]

sql_products = "INSERT INTO products (product_id, product_title, currency, current_price, target_price, timestamp, url, email_pref) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
cursor.executemany(sql_products, products)

# Creating Price History Table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS price_history (
        history_id INTEGER PRIMARY KEY AUTOINCREMENT,  
        product_id INTEGER,
        price REAL NOT NULL,
        date_checked DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (product_id) REFERENCES products (product_id)  
    )
''')

# Inserting Example Price History data into the Price History Table
price_history = [
    (1, 1, 199.99, '2024-08-08 19:26'),
    (2, 2, 5.00, '2024-08-08 19:26'),
    (3, 3, 27.88, '2024-08-08 19:26'),
    (4, 4, 19.69, '2024-08-08 19:26')
]

sql_price_history = "INSERT INTO price_history (history_id, product_id, price, date_checked) VALUES (?, ?, ?, ?)"
cursor.executemany(sql_price_history, price_history)

# Committing the Data Insertions and Closing the Connection to the Database
conn.commit()
cursor.close()
conn.close()
