def prepare_data_for_plotting(data):
    df = pd.DataFrame(data)
    df['timestamp'] = pd.to_datetime(df['timestamp'])  # Ensure the timestamp is in datetime format
    return df


import matplotlib.pyplot as plt


def plot_price_changes(df):
    plt.figure(figsize=(10, 6))

    for product_id in df['product_id'].unique():
        product_data = df[df['product_id'] == product_id]
        plt.plot(product_data['timestamp'], product_data['price'], marker='o', linestyle='-',
                 label=f'Product {product_id}')

    plt.title('Price Changes Over Time')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.savefig('price_changes.png')  # Save the figure as a .png file
    plt.show()  


from back_end.be_db_interactions import WebscrapingDbInteractions
import pandas as pd
import matplotlib.pyplot as plt


def fetch_data_for_visualization():
    db = WebscrapingDbInteractions()
    data = db.get_all_ws_results()  
    return data


def prepare_data_for_plotting(data):
    df = pd.DataFrame(data)
    df['timestamp'] = pd.to_datetime(df['timestamp'])  
    return df


def plot_price_changes(df):
    plt.figure(figsize=(10, 6))

    for product_id in df['product_id'].unique():
        product_data = df[df['product_id'] == product_id]
        plt.plot(product_data['timestamp'], product_data['price'], marker='o', linestyle='-',
                 label=f'Product {product_id}')

    plt.title('Price Changes Over Time')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.savefig('price_changes.png')  # Save the figure as a .png file
    plt.show()  # Display the figure


if __name__ == "__main__":
    data = fetch_data_for_visualization()
    df = prepare_data_for_plotting(data)
    plot_price_changes(df)
