import os.path
import sqlite3
def get_DB_data(sql_query: str): # SHAIRA TODO
    """
    Connects + interacts with DB with sql_query provided. Returns the fetched_data as tuple.
    :param sql_query:
    :return: fetched_data (tuple)
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


def get_username(): # SHAIRA TODO
    """
    Specific DB interaction to obtain user's username
    :return:
    """
    try:
        sql_query = """ SELECT username FROM userDetails""" #TODO to change with actual DB column/table names
        fetched_data = get_DB_data(sql_query)
        # Doesn't need to be mapped as it only fetched one value
        username = str(fetched_data).title()
    except ValueError:
        # In case the retrieved username was not stored as str
        print("ValueError: Could not retrieve user's name, the user's name has been set as 'visitor'")
        username = "visitor"
    return username


def db_exists():
    """
    Checks if a DB exists (i.e. if there is an existing user). Returns True or False.
    :return: True | False
    """
    path = './temporary_db_testing.json'     #Temporary file for testing logic before DB is set up
    # TODO replace with actual DB file path
    if os.path.isfile(path):
        return True
    else:
        return False


def get_product_id(product_title: str):
    """
    Gets a product's id from DB given the product title.
    :param product_title: str
    :return: product_id: int
    """

    return 12


def email_notifications_on(product_id: int):
    """
    Sets as TRUE the email notifications for a specific product given the product_id.
    :param product_id:
    :return:
    """
    return

def email_notifications_off(product_id: int):
    """
    Sets as FALSE the email notifications for a specific product given the product_id.
    :param product_id:
    :return:
    """
    return


def get_all_tracked_prod():
    """
    Returns a dict of all products tracked and their details
    :return: dict [
    """

    return [{'title': 'Full length mirror 120cm Black',
            'currency': '£',
            'price': '39.99',
            'timestamp': '2024-08-08 19:26',
            'url': 'https://www.amazon.co.uk/dp/B0BL6GJVZS',
            'email_notif': False},
            {'title': 'Amazon Tablet for kids',
             'currency': '£',
             'price': '299.99',
             'timestamp': '2024-08-08 19:26',
             'url': 'https://www.amazon.co.uk/dp/B0BL6GJVZS',
             'email_notif': False}
            ]
