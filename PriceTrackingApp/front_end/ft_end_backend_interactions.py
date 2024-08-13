def get_product_data(url): # VIOLETA TODO
    """
    Url webscraping. Retrieves the full data from an Amazon product given the url as parameter.
    :param url: str
    :return: dict {title, currency, price, timestamp, url, email_notif}
    """

    return {'title': 'Full length mirror 120cm Black',
            'currency': '£',
            'price': '199.99',
            'timestamp': '2024-08-08 19:26',
            'url': 'https://www.amazon.co.uk/dp/B0BL6GJVZS',
            'email_notif': False}
    # To set up 'email_notif' as False as default

def add_new_tracking(product_data):
    """
    Adds product data into to DB.
    :param product_data [dict {title, currency, price, timestamp, url}]
    :return: None
    """
    return