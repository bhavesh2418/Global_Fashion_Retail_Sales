import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load cleaned data
df = pd.read_csv("fashion_data/cleaned_transactions.csv")

# Check for negative values in financial columns
negative_lines = df[df['Line Total'] < 0]
negative_invoices = df[df['Invoice Total'] < 0]

print("\n✅ Negative Line Totals:", len(negative_lines))
print("\n✅ Negative Invoice Totals:", len(negative_invoices))

# Distribution of Unit Prices
plt.figure(figsize=(10, 5))
sns.histplot(df['Unit Price'], bins=50, kde=True)
plt.title("Distribution of Unit Prices")
plt.show()

# Distribution of Line Totals
plt.figure(figsize=(10, 5))
sns.histplot(df['Line Total'], bins=50, kde=True)
plt.title("Distribution of Line Totals")
plt.show()

print(df[df['Line Total'] < 0].head(10))
print(df[df['Invoice Total'] < 0].head(10))
