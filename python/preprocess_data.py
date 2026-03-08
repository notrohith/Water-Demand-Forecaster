import pandas as pd
import os
import sys

def preprocess(input_path, output_path):
    """
    Since data is already largely preprocessed, this function handles
    any final cleanups required before Haskell ingestion.
    """
    if not os.path.exists(input_path):
        print(f"Input file not found: {input_path}")
        return
        
    print(f"Preprocessing {input_path}...")
    df = pd.read_csv(input_path)
    
    # Fill any potential NaNs (though dataset is expected to be clean)
    df = df.fillna(0)
    
    # Ensure boolean columns are converted to int for easier Haskell parsing
    bool_cols = df.select_dtypes(include=['bool']).columns
    for col in bool_cols:
        df[col] = df[col].astype(int)
        
    # Standardize column names
    df.columns = [col.lower().replace(' ', '_') for col in df.columns]
    
    # Save the cleaned dataset
    df.to_csv(output_path, index=False)
    print(f"Saved preprocessed data to {output_path}")

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_dir = os.path.join(base_dir, 'data')
    
    input_file = os.path.join(data_dir, 'train_dataset.csv')
    output_file = os.path.join(data_dir, 'processed_water_dataset.csv')
    
    # Even though valid datasets are provided, we ensure processed_water_dataset is finalized
    preprocess(input_file, output_file)
