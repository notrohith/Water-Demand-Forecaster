import pandas as pd
import numpy as np
import os
import sys

def check_dataset(file_path):
    print(f"--- Checking {file_path} ---")
    if not os.path.exists(file_path):
        print(f"Error: {file_path} not found.")
        return False
    
    try:
        df = pd.read_csv(file_path)
    except Exception as e:
        print(f"Error loading {file_path}: {e}")
        return False
        
    print(f"Shape: {df.shape}")
    
    # Check for missing values
    missing = df.isnull().sum()
    if missing.sum() > 0:
        print("Missing values found in columns:")
        print(missing[missing > 0])
    else:
        print("No missing values.")
        
    # Check data types
    print("Data types summary:")
    print(df.dtypes.value_counts())
    
    # Basic statistics for a few key columns if they exist
    key_cols = ['total_water_consumption_billion_m3', 'water_scarcity_level']
    existing_keys = [c for c in key_cols if c in df.columns]
    if existing_keys:
        print("\nKey Columns Statistics:")
        print(df[existing_keys].describe())
        
    print("--------------------------------\\n")
    return True

if __name__ == "__main__":
    data_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data')
    datasets = ['train_dataset.csv', 'test_dataset.csv', 'processed_water_dataset.csv']
    
    success = True
    for ds in datasets:
        if not check_dataset(os.path.join(data_dir, ds)):
            success = False
            
    if not success:
        sys.exit(1)
    else:
        print("All datasets checked successfully.")
