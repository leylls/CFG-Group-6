import sqlite3

def fetch_data(sql_query):
    fetched_data = ""
    try:
        conn = sqlite3.connect("price_tracker.db")  # Use your actual database name here
        cur = conn.cursor()
        cur.execute(sql_query)  # For example, 'SELECT username FROM users' to get usernames
        fetched_data = cur.fetchall()
    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
    finally:
        if conn:
            conn.close()
    return fetched_data

# Example
# sql_query = "SELECT username FROM users"
# result = fetch_data(sql_query)
# print(result)

"""
Specific DB interaction to obtain user's username
:return: str
"""

def get_username():

    try:
        sql_query = "SELECT username FROM users"  # Actual DB column/table names
        fetched_data = fetch_data(sql_query)
        if fetched_data:
            username = str(fetched_data[0][0]).title()  # Access the first result
        else:
            username = "visitor"
    except ValueError:
        print("ValueError: Could not retrieve user's name, the user's name has been set as 'visitor'")
        username = "visitor"
    return username

# Example
# username = get_username()
# print(username)  # Output: First username from the users table or 'visitor'

"""
Inserts a new user into the DB.
:param user_details: dict
:return: None
"""

def update_user_details(user_details):

    try:
        conn = sqlite3.connect("price_tracker.db")
        cur = conn.cursor()

        # Prepare and execute the SQL query
        sql_query = """
        INSERT INTO users (username, email)
        VALUES (?, ?)
        """
        cur.execute(sql_query, (user_details['username'], user_details['user_email']))

        # Commit changes and close the connection
        conn.commit()
    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
    finally:
        if conn:
            conn.close()

# Example
# new_user_details = {'username': 'NewUser', 'user_email': 'newuser@example.com'}
# update_user_details(new_user_details)
# print("User details updated")

"""
Checking to see if a DB exists (i.e. if there is an existing user). Returns True or False.
:return: True | False
"""

import os

def db_exists():

    path = 'price_tracker.db'  # Actual DB file path
    return os.path.isfile(path)

# Example
# if db_exists():
#     print("Database exists")
# else:
#     print("Database does not exist")

"""
Sets email notifications as TRUE for a specific product given the product_id to turn on the notifications
:param product_id: int
:return: None
"""

def email_notifications_on(product_id: int):

    try:
        conn = sqlite3.connect("price_tracker.db")
        cur = conn.cursor()

        sql_query = "UPDATE products SET email_pref = 1 WHERE product_id = ?"
        cur.execute(sql_query, (product_id,))

        conn.commit()
    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
    finally:
        if conn:
            conn.close()

# Example
# email_notifications_on(1)
# print("Email notifications turned on for product ID 1")

"""
Sets email notifications as FALSE for a specific product given the product_id to turn off notifications
:param product_id: int
:return: None
"""

def email_notifications_off(product_id: int):

    try:
        conn = sqlite3.connect("price_tracker.db")
        cur = conn.cursor()

        sql_query = "UPDATE products SET email_pref = 0 WHERE product_id = ?"
        cur.execute(sql_query, (product_id,))

        conn.commit()
    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
    finally:
        if conn:
            conn.close()

# Example
# email_notifications_off(1)
# print("Email notifications turned off for product ID 1")


"""
Adding a new product into the DB.
:param product_data: dict
:return: None
"""

def add_new_tracking(product_data):

    try:
        conn = sqlite3.connect("price_tracker.db")
        cur = conn.cursor()

        sql_query = """
        INSERT INTO products (product_title, currency, current_price, timestamp, url)
        VALUES (?, ?, ?, ?, ?)
        """
        cur.execute(sql_query, (
            product_data['title'],
            product_data['currency'],
            product_data['price'],
            product_data['timestamp'],
            product_data['url']
        ))

        conn.commit()
    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
    finally:
        if conn:
            conn.close()

# Example
# new_product = {
#     'title': 'New_Product',
#     'currency': '£',
#     'price': '49.99',
#     'timestamp': '2024-08-08 19:26',
#     'url': 'https://www.example.com/product'
# }
# add_new_tracking(new_product)
# print("New product added to tracking")


"""
Gets a product's ID from the database using the product URL.
:param product_url: str
:return: product_id: int
"""
def get_product_id(product_url: str) -> int:

    product_id = None  # Initialize product_id to None
    try:
        conn = sqlite3.connect('price_tracker.db')
        cur = conn.cursor()
        sql_query = """SELECT product_id FROM products WHERE url = ?"""
        cur.execute(sql_query, (product_url,))
        fetched_data = cur.fetchone()
        if fetched_data:
            product_id = fetched_data[0]
        conn.close()
    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
    return product_id

# Example
# product_url = 'https://www.amazon.co.uk/dp/B0BL6GJVZS'
# product_id = get_product_id(product_url)
# print(f"Product ID for the URL '{product_url}' is: {product_id}")


"""
Retrieves the product price history log.
:param product_id: int
:param full_history: if False -> a partial 7-day history to be returned
:return: list of tuples (price, date_checked)
"""

def get_price_history(product_id: int, full_history: bool = False):

    price_history = []
    try:
        conn = sqlite3.connect('price_tracker.db')
        cur = conn.cursor()

        if full_history:
            sql_query = """SELECT price, date_checked FROM price_history WHERE product_id = ? ORDER BY date_checked DESC"""
            cur.execute(sql_query, (product_id,))
        else:
            sql_query = """SELECT price, date_checked FROM price_history WHERE product_id = ? 
                           AND date_checked >= datetime('now', '-7 days') ORDER BY date_checked DESC"""
            cur.execute(sql_query, (product_id,))

        price_history = cur.fetchall()
        conn.close()
    except sqlite3.Error as e:
        print(f"SQLite error: {e}")

    return price_history


# Example
# product_id = 1  # Replace with a valid product ID
# history = get_price_history(product_id, full_history=True)
# print(f"Full price history for product ID {product_id}: {history}")
