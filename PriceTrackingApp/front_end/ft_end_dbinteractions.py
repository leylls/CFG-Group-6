import os.path
import sqlite3

def get_username(): #TODO to change mock handlers to functional ones
    try:
        conn = sqlite3.connect("appdb.db") #mock db name
        cur = conn.cursor()
        cur.execute('select user_name from user_data') #mock column name and table name
        data_rows = cur.fetchall()
        conn.close()
        username = str(data_rows).title()
    except ConnectionError: #TODO add to python logs
        print("ConnectionError: Could not connect to Database, so the user's name has been set as 'visitor'")
        username = "visitor"
    except ValueError:
        print("ValueError: Could not retrieve user's name, the user's name has been set as 'visitor'")
        username = "visitor"
    return username

def db_exists(): #TODO
    """
    Checks if a DB exists (i.e. if there is an existing user). Returns True or False.
    :return: True | False
    """
    #path = './ft_end_utils.py'     #To test func
    # TODO replace with actual DB file path
    if os.path.isfile(path):
        return True
    else:
        return False
