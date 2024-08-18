from web_scraping import WebScraping
import sqlite3

# Get all urls user is monitoring from DB
def get_monitored_urls():
    conn = sqlite3.connect('price_tracker.db') 
    cur = conn.cursor()
    monitored_urls= cur.execute(
    '''
        SELECT p.url FROM products p
        INNER JOIN price_history h ON p.product_id = h.product_id
        WHERE p.email_pref = 'True'
    ''')
    cur.close()
    conn.close()
    return monitored_urls  #check if this returns a list

# Web scrape url_list
def get_ws_results(url_list):
    ws = WebScraping(url_list)
    web_scraping_results = ws.get_product_data()
    return web_scraping_results

def get_product_id_and_urls():
    conn = sqlite3.connect('price_tracker.db')
    cur = conn.cursor()
    product_id_and_urls = cur.execute(
    '''
        SELECT product_id,url FROM products p
        WHERE p.email_pref = 'True'
    ''')
    cur.close()
    conn.close()
    return product_id_and_urls #check if this returns a list of lists

def prepare_results_for_db(ws_results, product_id_and_urls):
    tuple_results = []
    for result in ws_results:
        for product_id, url in product_id_and_urls:
            if result['url'] == url:
                result['product_id'] = product_id
        tuple_results.append((result['product_id'], result['price'], result['currency'], result['timestamp']))
    return tuple_results

def insert_results_db(tuple_results):
    conn = sqlite3.connect('price_tracker.db') 
    cur = conn.cursor()
    cur.executemany('''
                INSERT INTO price_history(product_id,price,currency,date_checked)
                VALUES (?, ?, ?, ?)''', tuple_results)
    conn.commit()
    cur.close()
    conn.close()