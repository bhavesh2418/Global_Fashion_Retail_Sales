import os
import zipfile

# Kaggle dataset identifier
DATASET = "ricgomes/global-fashion-retail-stores-dataset"

# Ensure Kaggle API key is available
os.environ["KAGGLE_CONFIG_DIR"] = os.path.expanduser("~/.kaggle")  # Change path if needed

# Download dataset from Kaggle
print("\n📥 Downloading dataset...")
os.system(f"kaggle datasets download -d {DATASET}")

# Find the downloaded ZIP file
zip_file = None
for file in os.listdir():
    if file.endswith(".zip"):
        zip_file = file
        break

if zip_file:
    print(f"\n📂 Extracting {zip_file} ...")
    
    # Unzip the dataset
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall("fashion_data")  # Extract to 'fashion_data' folder
    
    # Delete the ZIP file after extraction
    os.remove(zip_file)
    print(f"\n🗑️ Deleted ZIP file: {zip_file}")

    print("\n✅ Dataset downloaded, extracted, and cleaned successfully!")
else:
    print("\n❌ No ZIP file found! Please check the dataset download.")
