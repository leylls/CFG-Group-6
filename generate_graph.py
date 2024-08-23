import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime, timedelta


def generate_price_data():
    # Simulate price data for 30 days
    dates = [datetime.now() - timedelta(days=i) for i in range(30)]
    dates.reverse()  # To ensure dates are in chronological order

    # Simulate price changes over time
    prices = np.random.uniform(low=90, high=110, size=len(dates)).round(2)

    return dates, prices


def generate_graph():
    dates, prices = generate_price_data()

    # Create a plot
    plt.figure(figsize=(10, 5))  # Optional: Specify the figure size
    plt.plot(dates, prices, marker='o', linestyle='-', color='b', label='Price')
    plt.title('Price Changes Over Time')
    plt.xlabel('Date')
    plt.ylabel('Price ($)')
    plt.xticks(rotation=45)  # Rotate date labels for better readability
    plt.tight_layout()  # Adjust layout to prevent clipping of labels
    plt.legend()

    # Save the plot as an image file
    filename = 'price_changes.png'
    plt.savefig(filename)
    plt.close()  # Close the plot to free up memory

    print(f"Graph saved as {filename}")


if __name__ == "__main__":
    generate_graph()
