import os

# Define the folder path
folder_path = "fashion_data"

# Get all CSV files in the folder
csv_files = [file for file in os.listdir(folder_path) if file.endswith(".csv")]

# Print the list of CSV file names
print("CSV files in the fashion_data folder:")
for file in csv_files:
    print(file)
