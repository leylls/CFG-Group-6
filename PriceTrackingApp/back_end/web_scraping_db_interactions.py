import sqlite3

class WebscrapingDbInteractions:
    
    def get_monitored_urls():                            
        conn = sqlite3.connect('back_end/price_tracker.db') 
        cur = conn.cursor()
        cur.execute(
        '''
            SELECT DISTINCT p.url FROM product_details p
            INNER JOIN price_history h ON p.product_id = h.product_id
            WHERE p.email_notif = True OR p.email_notif = 1;
        ''')
        monitored_urls = cur.fetchall()
        cur.close()
        conn.close()
        return [url[0] for url in monitored_urls]

    def get_product_id_and_urls():                       
        conn = sqlite3.connect('back_end/price_tracker.db')
        cur = conn.cursor()
        cur.execute(
        '''
            SELECT product_id, url FROM product_details
            WHERE email_notif = True or email_notif = 1;
        ''')
        product_id_and_urls = cur.fetchall()
        cur.close()
        conn.close()
        return [list(item) for item in product_id_and_urls]

    def insert_ws_results_db(tuple_results):                 # Insert results into DB
        conn = sqlite3.connect('back_end/price_tracker.db') 
        cur = conn.cursor()
        cur.executemany('''
                    INSERT INTO price_history(product_id, price, currency, timestamp)
                    VALUES (?, ?, ?, ?)''', tuple_results)
        conn.commit()
        cur.close()
        conn.close()