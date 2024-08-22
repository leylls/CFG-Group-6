import sqlite3

class DatabaseActions:

    def __init__(self):
        self.database = 'back_end/price_tracker.db'

    def fetch_data(self, query):
        try:
            conn = sqlite3.connect(self.database) 
            cur = conn.cursor()
            cur.execute(query)
            results = cur.fetchall()
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            results = []
        except Exception as e:
            print(f"Exception in _query: {e}")
            results = []
        finally:
            cur.close()
            conn.close()
        return results
    
    def insert_data(self, query, data):
        try:
            conn = sqlite3.connect(self.database) 
            cur = conn.cursor()
            cur.executemany(query, data)
            conn.commit()
        except sqlite3.Error as e:
            print(f"Database error: {e}")
        except Exception as e:
            print(f"Exception in _query: {e}")
        finally:
            cur.close()
            conn.close()

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
        self.insert_data(query, tuple_results)