import pandas as pd
import matplotlib.pyplot as plt

# Database interaction class
class DatabaseInteractions:
    def fetch_data(self, query):
        import sqlite3
        connection = sqlite3.connect("price_tracker.db")
        cursor = connection.cursor()
        cursor.execute(query)
        data = cursor.fetchall()
        connection.close()
        return data

    def get_price_history(self, product_id, full_history=False):
        if full_history:
            query = f"SELECT * FROM price_history WHERE product_id = {product_id}"
        else:
            query = f"SELECT * FROM price_history WHERE product_id = {product_id} AND timestamp >= datetime('now', '-7 days')"
        return self.fetch_data(query)

########## Fetch Data
db_interaction = DatabaseInteractions()
product_id = 7 # Replace with any product ID
full_history = True  # True for full history, False for last 7 days
price_history_data = db_interaction.get_price_history(product_id, full_history)

## Data for Visualization
def prepare_data_for_plotting(price_history_data):
    df = pd.DataFrame(price_history_data, columns=['product_id', 'price', 'currency', 'timestamp'])
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    return df

df = prepare_data_for_plotting(price_history_data)

#  Using Matplotlib
def plot_price_history(df, product_id):
    plt.figure(figsize=(10, 6))
    product_data = df[df['product_id'] == product_id]
    plt.plot(product_data['timestamp'], product_data['price'], marker='o', linestyle='-', label=f'Product {product_id}')
    plt.title(f'Price Changes Over Time for Product {product_id}')
    plt.xlabel('Date')
    plt.ylabel('Price £')
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

plot_price_history(df, product_id)
