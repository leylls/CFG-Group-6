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

def data_viz(prod_price_history): #TODO Ikram

    # Something that we can:
    return print("""

                (*) 14/08/24 -> £15.00
                (*) 13/08/24 -> £15.99
                (*) 12/08/24 -> £17.50
                (*) 11/08/24 -> £28.99
                (*) 10/08/24 -> £27.50
                (*) 09/08/24 -> £25.50
                (*) 08/08/24 -> £24.99 """)


