from back_end.web_scraping import WebScraping
import sqlite3

#CHANGE DB NAME, TABLE NAME AND COLUMN NAME
'''
db_name = price_tracking_app
table1 = product_details
table2= webscraping_results
'''

# Get all urls user is monitoring from DB
def get_monitored_urls():
    conn = sqlite3.connect('price_traking_app.db') 
    cur = conn.cursor()
    monitored_urls= cur.execute(
    '''
        SELECT p.url FROM product_details p
        INNER JOIN webscraping_results ws ON p.product_id = ws.product_id
        WHERE p.email_notification = 'True'
    ''')
    return monitored_urls  #check if this returns a list

# Web scrape url_list
def get_ws_results(url_list):
    ws = WebScraping(url_list)
    web_scraping_results = ws.get_product_data()
    return web_scraping_results

def get_product_id_and_urls():
    conn = sqlite3.connect('price_tracking_app.db')
    cur = conn.cursor()
    product_id_and_urls = cur.execute(
        '''
        SELECT product_id,url FROM product_details p
        WHERE p.email_notification = 'True'
    ''')
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
    conn = sqlite3.connect('price_tracking_app.db') 
    cur = conn.cursor()
    cur.executemany('''
                INSERT INTO webscraping_results(product_id,price,,currency, timestamp)
                VALUES (?, ?, ?, ?)''', tuple_results)
    conn.commit()