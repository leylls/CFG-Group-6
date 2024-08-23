import sqlite3
import os.path

class DatabaseActions:

    def __init__(self):
        self.database = os.path.join('back_end', 'price_tracker.db')

    def fetch_data(self, query):
        try:
            print(f">>> fetch_data >>>> about to connect. DB is {self.database}")
            conn = sqlite3.connect(self.database)
            print(f">>> fetch_data >>>> conn is {conn}")
            cur = conn.cursor()
            print(f">>> fetch_data >>>> cur is {cur}")
            cur.execute(query)
            print(f">>> fetch_data >>>> cur is {cur}")
            results = cur.fetchall()
            cur.close()
            conn.close()
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            results = []
        return results
    
    def change_data(self, query, data):
        try:
            conn = sqlite3.connect(self.database) 
            cur = conn.cursor()
            if isinstance(data, list):      #check if data is a list
                cur.executemany(query, data)
            else:
                cur.execute(query, data)
            conn.commit()
            cur.close()
            conn.close()
        except sqlite3.Error as e:
            print(f"Database error: {e}")


class FrontEndDbInteractions(DatabaseActions):

    def get_username(self):
        try:
            query = "SELECT username FROM user_details"
            fetched_data = self.fetch_data(query)
            if fetched_data:
                username = str(fetched_data[0][0]).title()
            else:
                username = "visitor"
        except ValueError:
            print("ValueError: Could not retrieve, user's name has been set as 'visitor'")
            username = "visitor"
        return username

    def get_user_details(self):
        query = "SELECT username, user_email, email_pref FROM user_details"
        fetched_data = self.fetch_data(query)
        if fetched_data:
            return {'username': fetched_data[0][0], 'user_email': fetched_data[0][1], 'email_pref': fetched_data[0][2]}
        return {}

    def insert_new_user_details(self, user_details):
        email_pref = 0
        if user_details['email_pref'] == "y":
            email_pref = 1
        query = """
            INSERT INTO user_details (username, user_email, email_pref)
            VALUES (?, ?, ?)
            """
        data = (user_details['username'], user_details['user_email'], email_pref)
        self.change_data(query, data)

    def update_user_detail(self, username = None, user_email = None, email_pref = None):
        """
        Updates one particular user_detail - given as the parameter.
        :param username: str
        :param user_email: str
        :param email_pref: bool
        :return:
        """
        if username:
            query = """
                    UPDATE user_details 
                    SET username = ?
                    """
            self.change_data(query, (username,))

        if user_email:
            query = """
                    UPDATE user_details 
                    SET user_email = ?
                    """
            self.change_data(query, (user_email,))

        if email_pref is not None:
            email_pref = 1 if email_pref else 0
            query = """
                    UPDATE user_details 
                    SET email_pref = ?
                    """
            self.change_data(query, (email_pref,))

    def db_exists(self):
        path = self.database
        return os.path.isfile(path)
    
    def get_product_id(self, product_url: str):
        query = f"SELECT product_id FROM product_details WHERE url = '{product_url}'"
        fetched_data = self.fetch_data(query)
        if fetched_data:
            return fetched_data[0][0]
        return None
    
    def product_email_notifications_toggle(self, product_details):
        if product_details['email_notif'] == 1:
            new_email_notif = 0
        else:
            new_email_notif = 1
        query = "UPDATE product_details SET email_notif = ? WHERE product_id = ?"
        self.change_data(query, (new_email_notif, product_details['product_id']))

    def product_change_target_price(self, product_details):
        query = "UPDATE product_details SET target_price = ? WHERE product_id = ?"
        data = (product_details['target_price'], product_details['product_id'])
        self.change_data(query, data)
    
    def get_all_tracked_prod(self):
        """
        Returns a dictionaries for all products tracked and their details.
        :return: dicts
        """
        query = '''
                SELECT 
                    pd.product_id, 
                    pd.product_title, 
                    pd.url, 
                    pd.target_price,
                    pd.email_notif,
                    ph.currency,
                    ph.price AS current_price
                FROM product_details pd
                LEFT JOIN price_history ph ON pd.product_id = ph.product_id
                AND ph.timestamp = (
                    SELECT MAX(timestamp)
                    FROM price_history
                    WHERE product_id = pd.product_id
                )
            '''
        product_data = self.fetch_data(query)

        # Prepare the user data structure
        all_tracked_products = []

        # Add product details to the user data structure
        for product in product_data:
            product_id, product_title, url, target_price, email_notif, currency, current_price = product
            all_tracked_products.append({
                'product_id': product_id,
                'title': product_title,
                'url': url,
                'target_price': target_price,
                'email_notif': email_notif,
                'currency': currency,
                'current_price': current_price})
        return all_tracked_products
    
    def add_new_tracking(self, product_data):
        try:
            conn = sqlite3.connect(self.database)
            cur = conn.cursor()
            # Inserting product_data into product_details table - autoincrementing product_id
            cur.execute(
                '''INSERT INTO product_details (product_title, currency, url, target_price, email_notif) 
                        VALUES (?, ?, ?, ?, ?)''',
                (product_data['title'], product_data['currency'], product_data['url'], product_data['target_price'], product_data['email_notif']))
            # Obtaining the product_id of the last entered product in product_details (as it is autoincrement)
            last_product_id = cur.lastrowid
            # Logging first webscraping log into price_history with the last inserted product's product_id
            cur.execute(
                '''INSERT INTO price_history (product_id, timestamp, currency, price) VALUES (?, ?, ?, ?)''',
                (last_product_id, product_data['timestamp'], product_data['currency'],product_data['price']))
            conn.commit()
            conn.close()
        except sqlite3.Error as e:
            print(f"Database error: {e}")
    
    def get_price_history(self, product_id, full_history=False):
        if full_history:
            query = f"SELECT * FROM price_history WHERE product_id = {product_id}"
        else:
            query = f"SELECT * FROM price_history WHERE product_id = {product_id} AND timestamp >= datetime('now', '-7 days')"
        return self.fetch_data(query)

    def stop_tracking(self, product_id):
        self.change_data("DELETE FROM product_details WHERE product_id = ?", (product_id,))
        self.change_data(" DELETE FROM price_history WHERE product_id = ?", (product_id,))
    
    def check_product_exists(self, url: str):
        """
        Checks if the url exists in the DB - if it DOES, it returns a ValueError - if it DOESNT, it
        continues.
        :param url: str
        :return:
        """
        conn = sqlite3.connect(self.database)
        cur = conn.cursor()
        cur.execute(f'SELECT EXISTS(SELECT url FROM product_details WHERE url="{url}")')
        exists = cur.fetchone()[0]
        cur.close()
        conn.close()
        if exists:
            return True
        else:
            return False


class EmailDbInteractions(DatabaseActions):
    def get_user_data(self):
        # Query 1: retrieve user details
        user_data_query = '''
            SELECT user_id, username, user_email
            FROM user_details
            WHERE email_pref = 1
            LIMIT 1
        '''
        user_data = self.fetch_data(user_data_query)

        if user_data:
            user_id, username, user_email = user_data[0]

            # Query 2: retrieve product details with the latest price and currency
            product_query = '''
                SELECT 
                    pd.product_id, 
                    pd.product_title, 
                    pd.url, 
                    pd.target_price,
                    ph.currency,
                    ph.price AS current_price
                FROM product_details pd
                LEFT JOIN price_history ph ON pd.product_id = ph.product_id
                WHERE pd.email_notif = 1
                AND ph.timestamp = (
                    SELECT MAX(timestamp)
                    FROM price_history
                    WHERE product_id = pd.product_id
                )
            '''
            product_data = self.fetch_data(product_query)

            # Prepare the user data structure
            user = {
                'user_id': user_id,
                'username': username,
                'email': user_email,
                'products': []
            }

            # Add product details to the user data structure
            for product in product_data:
                product_id, product_title, url, target_price, currency, current_price = product
                user['products'].append({
                    'product_id': product_id,
                    'product_title': product_title,
                    'url': url,
                    'target_price': target_price,
                    'currency': currency,
                    'current_price': current_price
                })

            return [user]  # Return a list of dictionaries for a single user
        else:
            return []  # Return an empty list if no user is found
        

class WebscrapingDbInteractions(DatabaseActions):
    
    def get_monitored_urls(self):                            
        query ='''
            SELECT DISTINCT p.url FROM product_details p
            INNER JOIN price_history h ON p.product_id = h.product_id
            WHERE p.email_notif = True OR p.email_notif = 1;
        '''
        monitored_urls = self.fetch_data(query)
        return [url[0] for url in monitored_urls]

    def get_product_id_and_urls(self):                       
        query = '''
            SELECT product_id, url FROM product_details
            WHERE email_notif = True OR email_notif = 1;
        '''
        product_id_and_urls = self.fetch_data(query)
        return [list(item) for item in product_id_and_urls]

    def insert_ws_results_db(self, tuple_results):
        query = '''
                    INSERT INTO price_history(product_id, price, currency, timestamp)
                    VALUES (?, ?, ?, ?)
        '''
        self.change_data(query, tuple_results)