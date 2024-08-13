import sqlite3


# Connecting to Existing Database or Creating New One
conn = sqlite3.connect('price_tracker.db')
cursor = conn.cursor()


# Creating Users Table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        username VARCHAR(100) NOT NULL,
        email VARCHAR(100) UNIQUE NOT NULL
    )
''')


# Inserting Example User data into the Users Table
users = [
    (1, 'Shaira', 'shaira@example.co.uk'),
    (2, 'Eva', 'eva@example.co.uk'),
    (3, 'Violeta', 'violeta@example.co.uk'),
    (4, 'Ikram', 'ikram@example.co.uk'),
    (5, 'Leyla', 'leyla@example.co.uk')
]

sql_users = "INSERT INTO users (user_id, username, email) VALUES (?, ?, ?)"
cursor.executemany(sql_users, users)


# Creating Products Table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        product_id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_title VARCHAR (1000) NOT NULL,
        currency VARCHAR (3),
        price DECIMAL (10, 2),
        timestamp DEFAULT CURRENT_TIMESTAMP,
        url NOT NULL
    )
''')


# Inserting Example Products from Web Scraped data into the Products Table
products = [
(1, 'Amazon Fire HD 10 Kids Pro tablet | ages 6–12, 10.1" brilliant screen, long battery life, parental controls, slim case, 2023 release, 32 GB, Happy Day', '£', '199.99', '2024-08-08 19:26', 'https://www.amazon.co.uk/dp/B0BL6GJVZS'),
(2, 'It Ends With Us: The emotional #1 Sunday Times bestseller, Now a major film starring Blake Lively and Justin Baldoni (Lily & Atlas, 1)', '£', '5.00', '2024-08-08 19:26', 'https://www.amazon.co.uk/Ends-Us-Colleen-Hoover/dp/1471156265/'),
(3, 'Mighty Patch Hero Cosmetics Original Patch - Hydrocolloid Acne Pimple Patch for Covering Zits and Blemishes, Spot Stickers for Face and Skin (36 Count)', '$', '27.88', '2024-08-08 19:26', 'https://www.amazon.com/Mighty-Patch-Hydrocolloid-Absorbing-count/dp/B074PVTPBW'),
(4, 'HP S1 8GB RAM DDR4 (1x8GB) Laptop Ram 3200 MHz SODIMM PC4-2500 CL22 Memory 1.2v - 2E2M5AA#ABB', '$', '19.69', '2024-08-08 19:26', 'https://www.amazon.com/HP-Single-3200MHz-Laptop-Memory/dp/B0948X9C9N/ref=sr_1_3?sr=8-3')
]

sql_products = "INSERT INTO products (product_id, product_title, currency, price, timestamp, url) VALUES (?, ?, ?, ?, ?, ?)"
cursor.executemany(sql_products, products)


# Committing the Data Insertions and Closing the Connection to the Database
conn.commit()
cursor.close()
conn.close()
