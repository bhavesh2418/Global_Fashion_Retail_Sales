import pandas as pd

# Load cleaned dataset
df = pd.read_csv("fashion_data/cleaned_transactions.csv")

# Summary statistics for numerical columns
print("\n✅ Summary Statistics (Numerical Columns):")
print(df.describe())

# Unique values per column
print("\n✅ Unique Values Count:")
print(df.nunique())
