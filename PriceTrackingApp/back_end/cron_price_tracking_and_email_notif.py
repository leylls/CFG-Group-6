from back_end.web_scraping import WebScraping
from back_end.web_scraping_db_interactions import WebscrapingDbInteractions
# from email_api import PriceAlert
# from email_api_db_interaction import notify_user_from_db


def get_ws_results(url_list):
    ws = WebScraping(url_list)
    web_scraping_results = ws.get_product_data()
    return web_scraping_results

def prepare_results_for_db(ws_results, product_id_and_urls):
    tuple_results = []
    for result in ws_results:
        for product_id, url in product_id_and_urls:
            if result['url'] == url:
                result['product_id'] = product_id
        tuple_results.append((result['product_id'], result['price'], result['currency'], result['timestamp']))
    return tuple_results


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


def cron_job_run():
    url_list = WebscrapingDbInteractions.get_monitored_urls()                   # Web scrape url_list
    web_scraping = get_ws_results(url_list)                                     # Get all urls user is monitoring from DB
    product_id_and_url = WebscrapingDbInteractions.get_product_id_and_urls()    # Obtain corresponding product_id for each url
    tuple_results = prepare_results_for_db (web_scraping, product_id_and_url)   # Map each url to it product_id & include pricing information retrieved
    WebscrapingDbInteractions.insert_ws_results_db(tuple_results)                  # Store new web scraping results in DB
    #add email notification functions