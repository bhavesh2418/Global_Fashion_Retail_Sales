import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load a single file
returns_by_product = pd.read_csv("fashion_data/total_returns_by_product.csv")

# Test visualization
plt.figure(figsize=(12, 6))
sns.barplot(x="Product ID", y="Quantity", data=returns_by_product, hue="Product ID", palette="viridis", legend=False)
plt.xlabel("Product ID")
plt.ylabel("Total Returns")
plt.title("Total Returns by Product")
plt.xticks(rotation=45)
plt.show()