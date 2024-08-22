from back_end.web_scraping import WebScraping
# from back_end.web_scraping_db_interactions import WebscrapingDbInteractions
from back_end.email_api import PriceAlert
# from back_end.email_api_db_interaction import notify_user_from_db, check_price_below_threshold

"""
I have commented out some of the imports to avoid issues as these are in process of refactoring (change names)
- Eva xx
"""

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

def notify_user_from_db(price_alert):
    email_db = EmailDbInteractions()
    user_data = email_db.get_user_data()

    if not user_data:
        print("No users found with email preferences enabled.")
        return

    emails_sent = 0
    for user in user_data:
        username = user['username']
        email = user['email']

        for product in user['products']:
            if check_price_below_threshold(product['current_price'], product['target_price']):
                try:
                    price_alert.send_alert(
                        recipient_email=email,
                        name=username,
                        product_name=product['product_title'],
                        current_price=product['current_price'],
                        threshold_price=product['target_price'],
                        product_url=product['url'],
                        currency=product['currency']
                    )
                    emails_sent += 1
                except Exception as e:
                    print(f"Failed to send email to {email}: {str(e)}")

    if emails_sent == 0:
        print("No emails sent. Check if any products are below their target prices.")
    else:
        print(f"Total emails sent: {emails_sent}")

def send_price_alert_email(price_alert):
    print("Activating price alert email notification...")
    notify_user_from_db(price_alert)
    print("Price alert email process completed.")


def cron_job_run():
    # Web scraping functions
    ws_db = WebscrapingDbInteractions()
    url_list = ws_db.get_monitored_urls()                                       # Web scrape url_list
    web_scraping = get_ws_results(url_list)                                     # Get all urls user is monitoring from DB
    product_id_and_url = ws_db.get_product_id_and_urls()                        # Obtain corresponding product_id for each url
    tuple_results = prepare_results_for_db (web_scraping, product_id_and_url)   # Map each url to it product_id & include pricing information retrieved
    ws_db.insert_ws_results_db(tuple_results)                                   # Store new web scraping results in DB
    # Email notification functions
    price_alert = PriceAlert(                                                   # Initialise with API credentials
        api_key='your_api_key',
        api_secret='your_api_secret',
        sender_email='group6.cfgdegree24@gmail.com'
    )
    send_price_alert_email(price_alert)                                         # Send email is latest price is below threshold price