import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

# Step 1: Define the mock data
mock_data = [
    (1, 1, '2024-08-20 22:00', '£', 46.99),
    (8, 1, '2024-08-22 14:00', '£', 50.99),
    (127, 1, '2024-08-23 08:53', '£', 42.5),
    (134, 1, '2024-08-24 10:51', '£', 42.5)
]

# Step 2: Convert mock data into a DataFrame
df = pd.DataFrame(mock_data, columns=['log_id', 'product_id', 'timestamp', 'currency', 'price'])

# Convert 'timestamp' to datetime object for proper plotting
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Check DataFrame contents for debugging
print("DataFrame:")
print(df)


# Step 3: Function to plot the data for a specific product ID
def plot_price_history(df, product_id):
    plt.figure(figsize=(10, 6))

    # Filter data for the specific product_id
    product_data = df[df['product_id'] == product_id]

    # Debugging: Check the filtered data
    print(f"Filtered Data for product_id {product_id}:")
    print(product_data)

    # Check if there's data to plot
    if product_data.empty:
        print(f"No data available for product ID: {product_id}")
        return

    # Plotting price over time
    plt.plot(product_data['timestamp'], product_data['price'], marker='o', linestyle='-', label=f'Product {product_id}')

    # Formatting the plot
    plt.title(f'Price Changes Over Time for Product {product_id}')
    plt.xlabel('Date')
    plt.ylabel('Price (£)')
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()

    # Add currency symbol to the y-axis
    plt.gca().yaxis.set_major_formatter(FuncFormatter(lambda x, _: f'£{x:.2f}'))

    # Save the plot as a PNG file or display it
    filename = f'product_{product_id}_price_history.png'
    plt.savefig(filename)
    plt.show()
    plt.close()  # Close the plot to free memory


# Step 4: Plot and save the graph for the specific product ID
product_id_to_plot = 1  # Change this to plot for different products
plot_price_history(df, product_id_to_plot)
