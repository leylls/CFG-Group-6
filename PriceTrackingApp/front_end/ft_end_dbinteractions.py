import os.path
import sqlite3
def get_DB_data(sql_query): # SHAIRA TODO
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
