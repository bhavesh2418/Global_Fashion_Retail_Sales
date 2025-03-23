import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
file_path = "fashion_data/transactions.csv"
df = pd.read_csv(file_path)

# ✅ Dataset Overview
print("\n✅ Dataset Overview:\n")
print(df.info())

# ✅ First 5 Rows
print("\n✅ First 5 Rows:\n")
print(df.head())

# ✅ Missing Values Count
print("\n✅ Missing Values Count:\n")
print(df.isnull().sum())

# ✅ Convert 'Date' column to datetime
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# ✅ Handle missing values (Fixed Warning)
df = df.fillna({'Size': 'Unknown', 'Color': 'Unknown'})

# ✅ Remove duplicates
duplicates = df.duplicated().sum()
print(f"\n✅ Duplicate Rows: {duplicates}")

if duplicates > 0:
    df = df.drop_duplicates()
    print("✅ Duplicates removed.")

# ✅ Outlier Detection
numeric_cols = ['Unit Price', 'Quantity', 'Discount', 'Line Total', 'Invoice Total']

plt.figure(figsize=(10, 5))
sns.boxplot(data=df[numeric_cols])
plt.xticks(rotation=45)
plt.title("Boxplot for Outlier Detection")
plt.show()

# ✅ Save cleaned data
df.to_csv("fashion_data/cleaned_transactions.csv", index=False)
print("\n✅ Data cleaning completed. Cleaned data saved as 'cleaned_transactions.csv'")
