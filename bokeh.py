from bokeh.plotting import figure, show, output_file
import pandas as pd

# Mock data
mock_data = [
    (1, 1, '2024-08-20 22:00', '£', 46.99),
    (8, 1, '2024-08-22 14:00', '£', 50.99),
    (127, 1, '2024-08-23 08:53', '£', 42.5),
    (134, 1, '2024-08-24 10:51', '£', 42.5)
]

# Convert to DataFrame
df = pd.DataFrame(mock_data, columns=['log_id', 'product_id', 'timestamp', 'currency', 'price'])
df['timestamp'] = pd.to_datetime(df['timestamp'])


def create_bokeh_plot(df, product_id):
    product_data = df[df['product_id'] == product_id]

    if product_data.empty:
        print(f"No data available for product ID: {product_id}")
        return

    # Define output file name
    filename = f'product_{product_id}_price_history.html'
    output_file(filename)

    # Create plot
    p = figure(x_axis_type='datetime', title=f'Price Changes Over Time for Product {product_id}', plot_width=800,
               plot_height=400)
    p.line(product_data['timestamp'], product_data['price'], line_width=2, legend_label=f'Product {product_id}',
           color='blue', marker='o')

    # Add axis labels
    p.xaxis.axis_label = 'Date'
    p.yaxis.axis_label = 'Price (£)'

    # Show the plot
    show(p)


# Generate and save the plot
create_bokeh_plot(df, product_id=1)
