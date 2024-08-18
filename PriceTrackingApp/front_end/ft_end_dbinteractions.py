import os.path
import sqlite3


def get_db_data(sql_query: str):
    """
    Connects + interacts with DB with sql_query provided. Returns the fetched_data as tuple.
    :param sql_query:
    :return: fetched_data (tuple)
    """

    """
    *** I made this originally to explore how to interact with the DB - I guess you can use it
    if you find it useful - if not, or you have coded something else already, you can just delete!
    - Eva xx
    """


    fetched_data = ""
    try:
        conn = sqlite3.connect("appdb.db") #To change with final db file name
        cur = conn.cursor()
        cur.execute(sql_query) # For example 'SELECT user_name FROM user_details' to get user's name
        fetched_data = cur.fetchall()
        conn.close()
    except ConnectionError:
        print("ConnectionError: Could not interact with Database, please check the file/tables queried do exist.")
    return fetched_data


def get_username():
    """
    Specific DB interaction to obtain user's username
    :return:
    """
    try:
        sql_query = """ SELECT username FROM userDetails""" #TODO to change with actual DB column/table names
        fetched_data = get_db_data(sql_query)
        # Doesn't need to be mapped as it only fetched one value
        username = str(fetched_data).title()
    except ValueError:
        # In case the retrieved username was not stored as str
        print("ValueError: Could not retrieve user's name, the user's name has been set as 'visitor'")
        username = "visitor"
    return username

def get_user_details():
    """
    Retrieves username and user_email from DB.
    :return: dict | {'username', 'user_email'}
    """
    return {'username': 'Eva', 'user_email': 'eva@cfg.com'}

def update_user_details(user_details):
    """
    Inserts updated user_details into de DB.
    :param user_details: dict
    :return:
    """

    """
    user_details will be a dict with a structure as:
    example_user_details = {'username': "Shaira"',
                'email_pref': "y"',
                'user_email': ""shaira@cfgdegree.com""'}
                
    ** Be mindful that as we have set email_pref to be a boolean in the DB 
    the "y" will need to be translated into such when inserted into the DB.
    """

    return


def db_exists():
    """
    Checks if a DB exists (i.e. if there is an existing user). Returns True or False.
    :return: True | False
    """
    path = 'back_end/price_tracker.db'
    if os.path.isfile(path):
        return True
    else:
        return False


def get_product_id(product_url: str):
    """
    Gets a product's id from DB given the product title.
    :param product_url: str
    :return: product_id: int
    """

    return 12


def email_notifications_on(product_id: int):
    """
    Sets as TRUE the email notifications for a specific product given the product_id.
    i.e. to update value in the products (product_id) 'email_pref' column as 1
    :param product_id:
    :return:
    """
    return

def email_notifications_off(product_id: int):
    """
    Sets as FALSE the email notifications for a specific product given the product_id.
    i.e. to update value in the products (product_id) 'email_pref' column as 0
    :param product_id:
    :return:
    """
    return


def get_all_tracked_prod():
    """
    Returns a dict of all products tracked and their details
    :return: dict
    """

    return [{'id': 1,
             'title': 'Full length mirror 120cm Black',
            'currency': '£',
            'price': '39.99',
            'timestamp': '2024-08-08 19:26',
            'url': 'https://www.amazon.co.uk/dp/B0BL6GJVZS',
            'email_notif': False},
            {'id': 2,
             'title': 'Amazon Tablet for kids',
             'currency': '£',
             'price': '299.99',
             'timestamp': '2024-08-08 19:26',
             'url': 'https://www.amazon.co.uk/dp/B0BL6GJVZS',
             'email_notif': False}
            ]


def add_new_tracking(product_data):
    """
    Adds product data into to DB.
    :param product_data [dict {title, currency, price, timestamp, url}]
    :return: None
    """
    pass


def get_price_history(produc_id, full_history=False):
    """
     Retrieves the product price history log.
    :param produc_id: int
    :param full_history: if False -> a partial 7-day history to be returned
    :return:
    """

    return #TODO ask Ikram the data type she needs to then make data viz


def stop_tracking(product_id):
    """
    Deletes the product from the user's list of tracked products.
    :param product_id: int
    :return:
    """

    return

