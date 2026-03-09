import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib
import os
import numpy as np

def train_and_save_model():
    print("Loading dataset...")
    data_path = 'c:/Users/123sr/OneDrive/Desktop/Haskell Project/data/processed_water_dataset.csv'
    df = pd.read_csv(data_path)
    
    # Selected features corresponding to Dashboard inputs
    features = [
        'per_capita_water_use_l_per_day', # Will map to Population Indicator
        'industrial_water_use_percent',
        'agricultural_water_use_percent',
        'water_scarcity_level',
        'lag_1',
        'lag_2'
    ]
    target = 'total_water_consumption_billion_m3'
    
    # Drop rows with NaNs in necessary columns
    df = df.dropna(subset=features + [target])
    
    X = df[features]
    y = df[target]
    
    print("Training Random Forest Regressor...")
    model = RandomForestRegressor(n_estimators=100, random_state=42, max_depth=10)
    model.fit(X, y)
    
    # Save the model
    output_dir = 'c:/Users/123sr/OneDrive/Desktop/Haskell Project/output'
    os.makedirs(output_dir, exist_ok=True)
    model_path = os.path.join(output_dir, 'rf_model.joblib')
    
    joblib.dump(model, model_path)
    
    # Also save the scaler max values to use them in dashboard to map normalized inputs
    max_values = X.max().to_dict()
    max_values_path = os.path.join(output_dir, 'feature_max_vals.json')
    import json
    with open(max_values_path, 'w') as f:
        json.dump(max_values, f)
        
    print(f"Model saved to {model_path}")
    print(f"Feature max values saved to {max_values_path}")

if __name__ == '__main__':
    train_and_save_model()
