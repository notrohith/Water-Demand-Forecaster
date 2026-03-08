AGENTS.md
Project

Projected Water Demand Forecasting in Water-Stressed Urban Basins Using Recursive Aggregation Models

Architecture:

Haskell Forecast Engine
        +
Python Data Processing
        +
Streamlit Visualization Dashboard
1. Purpose

This document defines how AI agents must interact with and modify the codebase.

Agents must follow these goals:

preserve the Haskell forecasting engine

maintain Python preprocessing and integration

maintain Streamlit visualization dashboard

avoid architectural drift

The project demonstrates functional programming (Haskell) applied to predictive water demand forecasting.

2. System Architecture

The system is composed of three layers.

Dataset (CSV)
      ↓
Python Preprocessing
      ↓
Feature Aggregation
      ↓
Haskell Recursive Forecast Engine
      ↓
Prediction Output
      ↓
Streamlit Dashboard
Architecture Rule

Agents must not move forecasting logic out of Haskell.

Python and Streamlit only handle:

preprocessing

integration

visualization

3. Project Directory Structure

Agents must preserve this structure.

water-demand-forecast/

data/
    water_dataset.csv

haskell/
    ForecastEngine.hs

python/
    preprocess_data.py
    run_forecast.py

dashboard/
    app.py

output/
    predictions.csv

docs/
    PRD.md
    TDD.md
    DESIGN.md
    TECHSTACK.md

AGENTS.md
README.md

Agents must not introduce unrelated directories.

4. Agent Responsibilities
4.1 Data Processing Agent

Responsible for dataset preparation.

Tasks:

load CSV datasets

clean column names

handle missing values

generate lag features

normalize numeric variables

Output:

processed_dataset.csv

Constraints:

do not modify demand values incorrectly

maintain chronological ordering

4.2 Feature Engineering Agent

Responsible for aggregating environmental variables.

Example aggregation:

DemandScore =
w1 × PerCapitaWaterUse
+ w2 × RainfallImpact
+ w3 × GroundwaterDepletionRate
+ w4 × AgriculturalWaterUse

Output:

aggregated_features.csv
4.3 Haskell Forecast Agent

This agent manages the core forecasting engine.

Responsibilities:

implement recursive forecasting algorithm

process aggregated dataset

generate multi-year demand predictions

Forecast formula:

Demand(t) =
α × Demand(t−1)
+ β × AggregatedFactors(t)

Constraints:

recursion must be used

functions must remain pure

avoid mutable state

4.4 Integration Agent

Responsible for communication between Python and Haskell.

Responsibilities:

pass processed dataset to Haskell engine

execute Haskell program

read forecast output

return results to dashboard

Integration workflow:

Python preprocessing
        ↓
Call Haskell engine
        ↓
Haskell generates predictions
        ↓
Python reads output
4.5 Visualization Agent

Responsible for building the Streamlit dashboard.

Dashboard features:

dataset upload

forecast execution

prediction graphs

results table

evaluation metrics

Visualization components:

historical demand trend

predicted demand trend

comparison graphs

performance metrics

5. Coding Rules
General Rules

Agents must:

preserve modular architecture

avoid unnecessary dependencies

write readable and documented code

maintain separation between modules

Haskell Rules

use pure functions

avoid side effects

use recursion for forecasting logic

define strong data types

Example structure:

WaterRecord
ForecastResult
Python Rules

pandas must be used for preprocessing

integration logic must remain in python/

do not move forecasting logic into Python

Streamlit Rules

UI must remain minimalistic

focus on graphs and analytics

avoid unnecessary styling complexity

6. Execution Workflow

Agents must follow this order:

1 Dataset loading
2 Data preprocessing
3 Feature aggregation
4 Run Haskell forecasting engine
5 Generate prediction output
6 Visualize results in Streamlit

Agents must not skip steps.

7. Anti-Hallucination Safeguards

Agents must follow these safeguards to prevent incorrect code generation.

7.1 No Invented APIs

Agents must not create or reference:

non-existent Haskell libraries

fictional APIs

unsupported Streamlit functions

If uncertain, agents must request clarification rather than guessing.

7.2 No Architecture Drift

Agents must never:

move forecasting logic into Python

remove the Haskell forecasting engine

replace recursion with unrelated ML models

7.3 No Fake Data Assumptions

Agents must not assume dataset structure without verification.

Before processing data, agents must check dataset columns.

Example validation:

Year
Total Water Consumption
Rainfall Impact
Groundwater Depletion Rate
7.4 Deterministic Output

Forecast results must be reproducible.

Agents must avoid:

random parameter changes

non-deterministic algorithms

7.5 Explicit Error Handling

Agents must implement validation checks for:

missing columns

invalid data types

empty datasets

failed Haskell execution

Error messages must be clear.

8. Testing Requirements

Agents must verify:

preprocessing pipeline

Haskell recursion engine

Python-Haskell integration

Streamlit visualization

Tests must confirm that:

predictions generate correctly

graphs render correctly

evaluation metrics compute accurately

9. Security and Data Integrity

Agents must ensure:

dataset values are not modified unintentionally

prediction outputs remain traceable

file operations avoid overwriting raw datasets

10. Success Criteria

The project is considered complete when:

Haskell recursive forecasting model produces predictions

Python integration successfully executes the Haskell engine

Streamlit dashboard visualizes results

demand forecasts respond to scenario changes

The final system must be suitable for academic presentation and capstone evaluation.