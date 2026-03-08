import pandas as pd
import os

def engineer_features(input_path, output_path):
    """
    Generates synthetic composite demand score or other features
    if the models or backend require it.
    """
    if not os.path.exists(input_path):
        print(f"Error: {input_path} not found.")
        return
        
    print(f"Engineering features from {input_path}...")
    df = pd.read_csv(input_path)
    
    # Example feature: Aggregate Demand Pressure
    # Combining water scarcity, per capita use and industrial usage percent
    if all(c in df.columns for c in ['water_scarcity_level', 'per_capita_water_use_l_per_day', 'industrial_water_use_percent']):
        df['demand_pressure_index'] = (
            df['water_scarcity_level'] * 0.4 +
            df['per_capita_water_use_l_per_day'] * 0.3 +
            df['industrial_water_use_percent'] * 0.3
        )
        print("Added 'demand_pressure_index' feature.")
        
    # Save engineered dataset
    df.to_csv(output_path, index=False)
    print(f"Saved engineered datasets to {output_path}")

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_dir = os.path.join(base_dir, 'data')
    
    input_file = os.path.join(data_dir, 'processed_water_dataset.csv')
    # Can overwrite or save as a new version
    output_file = os.path.join(data_dir, 'engineered_water_dataset.csv')
    
    engineer_features(input_file, output_file)
