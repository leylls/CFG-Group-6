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

    return web_scraping_results[0]

def data_viz(prod_price_history): #TODO Ikram

    return "" # Something that I can print()