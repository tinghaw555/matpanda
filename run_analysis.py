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
highest= df.loc[df['revenue'].idxmax()]
# Create and save a simple bar plot
plt.figure(figsize=(8, 5))
plt.bar(df['product'], df['revenue'])
plt.title('Revenue by Product')
plt.ylabel('Revenue ($)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('revenue_plot.png')

print("✅ Done! Check for sales_with_revenue.csv and revenue_plot.png")