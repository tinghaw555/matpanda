# You can modify this file if you want
import pandas as pd
import matplotlib.pyplot as plt
from helpers import add_revenue

# Load data
df = pd.read_csv('sales.csv')

# Add revenue column using the provided function
df = add_revenue(df)

# Save updated CSV
df.to_csv('sales_with_revenue.csv', index=False)

max_row =df.loc[df['revenue'].idxmax()]
max_revenue = max_row['revenue']
product = max_row['product']

# Create and save a simple bar plot
plt.figure(figsize=(8, 5))
plt.bar(df['product'], df['revenue'])
plt.title('Revenue by Product')
plt.ylabel('Revenue ($)')
plt.xlabel('Product')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('revenue_plot.png')

print(f'the highest revenue is {max_revenue} and it is {product}')
print("✅ Done! Check for sales_with_revenue.csv and revenue_plot.png")
