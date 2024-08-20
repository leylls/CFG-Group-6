from back_end.web_scraping import WebScraping
import sqlite3
# from email_api import PriceAlert
# from email_api_db_interaction import notify_user_from_db


def get_monitored_urls():                                   # Get all urls user is monitoring from DB
    conn = sqlite3.connect('price_tracker.db') 
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


def get_ws_results(url_list):                               # Web scrape url_list
    ws = WebScraping(url_list)
    web_scraping_results = ws.get_product_data()
    return web_scraping_results

def get_product_id_and_urls():                              # Obtain corresponding product_id for each url
    conn = sqlite3.connect('price_tracker.db')
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

def prepare_results_for_db(ws_results, product_id_and_urls):  # Map each url to it product_id
    tuple_results = []
    for result in ws_results:
        for product_id, url in product_id_and_urls:
            if result['url'] == url:
                result['product_id'] = product_id
        tuple_results.append((result['product_id'], result['price'], result['currency'], result['timestamp']))
    return tuple_results

def insert_results_db(tuple_results):                       # Insert results into DB
    conn = sqlite3.connect('price_tracker.db') 
    cur = conn.cursor()
    cur.executemany('''
                INSERT INTO price_history(product_id, price, currency, timestamp)
                VALUES (?, ?, ?, ?)''', tuple_results)
    conn.commit()
    cur.close()
    conn.close()

def check_price_below_threshold(current_price, threshold_price):
    return float(current_price) < float(threshold_price)

def send_price_alert_email():
    print("Activating price alert email notification...")
    # initialise PriceAlert with API credentials
    price_alert = PriceAlert(
        api_key= 'your_api_key',
        api_secret='your_api_secret',
        sender_email='group6.cfgdegree24@gmail.com'
    )
    notify_user_from_db(price_alert)
    print("Price alert email process completed.")


#   FOR TESTING PURPOSES - TO BE RUN FROM MAIN

# url_list = get_monitored_urls()
# ws_results = get_ws_results(url_list)
# product_id_and_urls = get_product_id_and_urls()
# tuple_results = prepare_results_for_db(ws_results, product_id_and_urls)
# insert_results_db(tuple_results)