TODO.md
Project

Projected Water Demand Forecasting in Water-Stressed Urban Basins Using Recursive Aggregation Models

Architecture:

Haskell Forecast Engine
        +
Python Data Processing
        +
Streamlit Visualization Dashboard
Phase 1 — Project Initialization
1. Create Project Repository

Initialize the project folder.

water-demand-forecast/

Create base structure:

water-demand-forecast/

data/
haskell/
python/
dashboard/
output/
docs/

Create base documentation files:

README.md
PRD.md
TDD.md
DESIGN.md
TECHSTACK.md
AGENTS.md
TODO.md
Phase 2 — Dataset Setup
2. Add Dataset

Place dataset in:

data/water_dataset.csv

Dataset should include columns such as:

Country
Year
Total Water Consumption
Per Capita Water Use
Agricultural Water Use
Industrial Water Use
Rainfall Impact
Groundwater Depletion Rate
Water Scarcity Level
3. Validate Dataset

Create script:

python/check_dataset.py

Tasks:

load dataset

verify required columns

print dataset summary

detect missing values

Phase 3 — Data Preprocessing
4. Implement Preprocessing Script

Create file:

python/preprocess_data.py

Responsibilities:

clean column names

convert numeric columns

handle missing values

normalize data

generate lag features

encode categorical variables

Output:

output/processed_dataset.csv
5. Feature Aggregation

Create module:

python/feature_engineering.py

Compute aggregated demand score.

Example formula:

DemandScore =
w1 × PerCapitaWaterUse
+ w2 × RainfallImpact
+ w3 × GroundwaterDepletionRate
+ w4 × AgriculturalWaterUse

Output:

output/aggregated_features.csv
Phase 4 — Haskell Forecast Engine
6. Implement Haskell Forecast Module

Create file:

haskell/ForecastEngine.hs

Responsibilities:

load aggregated dataset

compute recursive demand predictions

output forecast values

Define data structure:

WaterRecord
ForecastResult
7. Implement Recursive Forecast Function

Forecast formula:

Demand(t) =
α × Demand(t−1)
+ β × AggregatedFactor(t)

Recursive function should:

read previous demand value

apply recursive formula

generate next prediction

Output file:

output/predictions.csv
Phase 5 — Python–Haskell Integration
8. Create Forecast Runner

Create file:

python/run_forecast.py

Responsibilities:

call Haskell forecasting engine

pass processed dataset

retrieve prediction output

Example flow:

python preprocessing
        ↓
call Haskell program
        ↓
read predictions.csv
Phase 6 — Model Evaluation
9. Implement Evaluation Metrics

Create module:

python/evaluate_model.py

Compute metrics:

MAE
RMSE

Output:

evaluation_results.json
Phase 7 — Streamlit Dashboard
10. Create Dashboard

Create file:

dashboard/app.py

Dashboard components:

Dataset Upload
Forecast Controls
Prediction Graph
Results Table
Evaluation Metrics
11. Implement Dataset Upload

Streamlit component:

st.file_uploader()

Tasks:

upload CSV dataset

preview data

pass dataset to preprocessing pipeline

12. Implement Forecast Execution

Add button:

Run Forecast

When pressed:

run preprocessing

run Haskell forecast engine

load predictions

13. Implement Visualization

Use Plotly charts to display:

Historical demand
Predicted demand
Combined trend graph
Phase 8 — Scenario Simulation
14. Add Scenario Controls

Allow user to modify:

Rainfall Impact
Groundwater Depletion
Per Capita Water Use

Dashboard should recompute forecasts dynamically.

Phase 9 — Testing
15. Unit Testing

Verify:

dataset preprocessing
feature aggregation
Haskell recursion
Python–Haskell integration
dashboard visualization
16. Integration Testing

Run full pipeline:

Dataset
↓
Preprocessing
↓
Haskell Forecast Engine
↓
Prediction Output
↓
Streamlit Visualization

Ensure predictions appear correctly.

Phase 10 — Final Project Preparation
17. Documentation Review

Ensure all documents exist:

PRD
TDD
Design Document
Tech Stack
Agents.md
18. Demo Preparation

Prepare demo flow:

Upload dataset
↓
Run forecast
↓
Display predictions
↓
Show demand trend graph
Final System Pipeline
Dataset
↓
Python Preprocessing
↓
Feature Aggregation
↓
Haskell Recursive Forecast Engine
↓
Prediction Output
↓
Streamlit Dashboard Visualization
Final Deliverables

The project must produce:

ForecastEngine.hs
preprocess_data.py
run_forecast.py
app.py
processed_dataset.csv
predictions.csv

and documentation.