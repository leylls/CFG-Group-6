
import os.path
import sqlite3


# 1. Connects and interacts with the database
def get_db_data(sql_query: str):
    fetched_data = ""
    try:
        conn = sqlite3.connect("back_end/price_tracker.db")  # Connect to the correct database file
        cur = conn.cursor()
        cur.execute(sql_query)
        fetched_data = cur.fetchall()
        conn.close()
    except sqlite3.Error as e:
        print(f" Connection Database error, please check file: {e}")
    return fetched_data


# 2. Fetches the user's username from the user_details table.
def get_username():
    try:
        sql_query = "SELECT username FROM user_details"
        fetched_data = get_db_data(sql_query)
        if fetched_data:
            username = str(fetched_data[0][0]).title()
        else:
            username = "visitor"
    except ValueError:
        print("ValueError: Could not retrieve,user's name has been set as 'visitor'")
        username = "visitor"
    return username


# 3. Fetches the user's username and email from the user_details table.
def get_user_details():
    sql_query = "SELECT username, user_email FROM user_details"
    fetched_data = get_db_data(sql_query)
    if fetched_data:
        return {'username': fetched_data[0][0], 'user_email': fetched_data[0][1]}
    return {}


# 4. Updates the user_details table
def update_user_details(user_details):

    try:
        conn = sqlite3.connect("price_tracker.db")
        cur = conn.cursor()
        sql_query = """
        INSERT INTO user_details (username, user_email)
        VALUES (?, ?)
        """
        cur.execute(sql_query, (user_details['username'], user_details['user_email']))
        conn.commit()
    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
    finally:
        if conn:
            conn.close()



# 5. Checking DB exits
def db_exists():
    path = 'price_tracker.db'
    return os.path.isfile(path)



# 6. Gets a product's ID from the product_details using URL
def get_product_id(product_url: str):
    sql_query = f"SELECT product_id FROM product_details WHERE url = '{product_url}'"
    fetched_data = get_db_data(sql_query)
    if fetched_data:
        return fetched_data[0][0]
    return None


# 7. email_notif to ON.
def email_notifications_on(product_id: int):
    try:
        conn = sqlite3.connect("price_tracker.db")
        cur = conn.cursor()
        cur.execute("UPDATE product_details SET email_notif = 1 WHERE product_id = ?", (product_id,))
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print(f"Database  error: {e}")


# 8.  email_notif to FALSE.
def email_notifications_off(product_id: int):
    try:
        conn = sqlite3.connect("price_tracker.db")
        cur = conn.cursor()
        cur.execute("UPDATE product_details SET email_notif = 0 WHERE product_id = ?", (product_id,))
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print(f"Database  error: {e}")


# 9. all tracked products
def get_all_tracked_prod():
    """
    Returns a dictionaries for all products tracked and their details.
    :return: dicts
    """
    tracked_products = []
    try:
        # Select all product details from the product_details table
        sql_query = """
        SELECT product_id, product_title, url, target_price, email_notif
        FROM product_details
        """
        fetched_data = get_db_data(sql_query)
        for row in fetched_data:
            tracked_products.append({
                'id': row[0],
                'title': row[1],
                'url': row[2],
                'target_price': row[3],
                'email_notif': bool(row[4])
            })
    except Exception as e:
        print(f"Database error: {e}")
    return tracked_products

# 10. Adds a new product to the product_details table.
def add_new_tracking(product_data):
    try:
        conn = sqlite3.connect("price_tracker.db")
        cur = conn.cursor()
        cur.execute('''INSERT INTO product_details (product_title, url, target_price, email_notif) 
                       VALUES (?, ?, ?, ?)''',
                       (product_data['title'], product_data['url'], product_data['price'], product_data.get('email_notif', 0)))
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print(f"Database error: {e}")


# 11. Retrieves the price history for a product. - 7DAYS
def get_price_history(product_id, full_history=False):
    if full_history:
        sql_query = f"SELECT * FROM price_history WHERE product_id = {product_id}"
    else:
        sql_query = f"SELECT * FROM price_history WHERE product_id = {product_id} AND timestamp >= datetime('now', '-7 days')"
    return get_db_data(sql_query)


# 12. Stops tracking a product
def stop_tracking(product_id):
    try:
        conn = sqlite3.connect("price_tracker.db")
        cur = conn.cursor()
        cur.execute("DELETE FROM product_details WHERE product_id = ?", (product_id,))
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print(f"Database error: {e}")


