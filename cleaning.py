import os
import pandas as pd

# Define input and output directories
data_dir = "fashion_data"
cleaned_dir = os.path.join(data_dir, "cleaned")
os.makedirs(cleaned_dir, exist_ok=True)

# List all CSV files in the dataset folder
datasets = [f for f in os.listdir(data_dir) if f.endswith(".csv")]

# Function to clean datasets
def clean_dataset(file_name):
    file_path = os.path.join(data_dir, file_name)
    df = pd.read_csv(file_path)
    print(f"\n🔍 Cleaning {file_name} ...")
    
    # Remove duplicates
    duplicates = df.duplicated().sum()
    if duplicates:
        print(f"✅ Duplicate Rows: {duplicates} (Removed)")
        df = df.drop_duplicates()
    
    # Handle missing values
    missing_values = df.isnull().sum()
    print("✅ Missing Values Before Cleaning:")
    print(missing_values[missing_values > 0])
    
    for col in df.columns:
        if df[col].dtype == "object":
            df[col].fillna("Unknown", inplace=True)
        else:
            df[col].fillna(df[col].median(), inplace=True)
    
    # Save cleaned data
    cleaned_file_path = os.path.join(cleaned_dir, file_name)
    df.to_csv(cleaned_file_path, index=False)
    print(f"✅ Cleaned file saved: {cleaned_file_path}")

# Apply cleaning to all files
for dataset in datasets:
    clean_dataset(dataset)

print("\n🎉 Data Cleaning Completed for All Files!")
