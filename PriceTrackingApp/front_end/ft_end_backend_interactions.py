from back_end.web_scraping import WebScraping

def get_product_data(url):
    """
    Url webscraping. Retrieves the full data from an Amazon product given the url as parameter.
    :param url: str
    :return: dict {title, currency, price, timestamp, url, email_notif}
    """
    ws = WebScraping([url])
    web_scraping_results = {}
    web_scraping_results = ws.get_product_data()
    web_scraping_results[0]['email_notif'] = False
    web_scraping_results[0]['target_price'] = 0

    return web_scraping_results[0]

def data_viz(prod_price_history):
    i = 1
    entry_no = 1
    prices = []
    dates = []
    for entry in prod_price_history:
        if i == 1 or entry[4] != prod_price_history[i - 2][4]:
            print(f"       ({entry_no})      Date: {entry[2][:-6]} ->  Price: {entry[3]}{entry[4]}")
            entry_no += 1
            prices.append(entry[4])
            dates.append(entry[2][:-6])
        i += 1
