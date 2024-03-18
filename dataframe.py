import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# Function to generate random timestamps
def random_dates(start, end, n):
    delta = end - start
    return [start + timedelta(seconds=random.randint(0, delta.total_seconds())) for _ in range(n)]

# Generate random data
start_date = datetime(2024, 3, 18, 9, 0, 0)
end_date = datetime(2024, 3, 18, 16, 0, 0)
timestamps = random_dates(start_date, end_date, 100)
product_ids = ['AAPL', 'GOOG', 'MSFT', 'AMZN']
products = [random.choice(product_ids) for _ in range(100)]
opens = [random.uniform(100, 200) for _ in range(100)]
highs = [o + random.uniform(0, 10) for o in opens]
lows = [o - random.uniform(0, 10) for o in opens]
closes = [random.uniform(low, high) for low, high in zip(lows, highs)]

# Create DataFrame
data = {
    'timestamp': timestamps,
    'product_id': products,
    'open': opens,
    'high': highs,
    'low': lows,
    'close': closes
}
stock_df = pd.DataFrame(data)
# Save DataFrame to CSV file
stock_df.to_csv('stock_market_data.csv', index=False)
print(stock_df)
