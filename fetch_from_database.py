from back_end.be_db_interactions import WebscrapingDbInteractions
import pandas as pd

def fetch_data_for_visualization():
    db = WebscrapingDbInteractions()
    data = db.get_all_ws_results()  # Adjust method name as needed
    return data
