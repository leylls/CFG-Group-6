import os.path
import sqlite3
def DB_interaction(sql_query):
    fetched_data = ""
    try:
        conn = sqlite3.connect("appdb.db") #mock db name
        cur = conn.cursor()
        cur.execute('select user_name from user_data') #mock column name and table name
        fetched_data = cur.fetchall()
        conn.close()
        username = str(fetched_data).title()
    except ConnectionError: #TODO add to python logs
        print("ConnectionError: Could not connect to Database, so the user's name has been set as 'visitor'")
        username = "visitor"
    return fetched_data


def get_username():
    try:
        sql_query = """ SELECT username FROM userDetails"""
        fetched_data = DB_interaction(sql_query)
        username = str(fetched_data).title()
    except ValueError:
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
