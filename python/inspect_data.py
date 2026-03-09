import pandas as pd
import json

df = pd.read_csv('c:/Users/123sr/OneDrive/Desktop/Haskell Project/data/processed_water_dataset.csv')
with open('c:/Users/123sr/OneDrive/Desktop/Haskell Project/data/columns.json', 'w') as f:
    json.dump(df.columns.tolist(), f)
