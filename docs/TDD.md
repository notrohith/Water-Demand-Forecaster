Technical Design Document (TDD)
Project Title

Projected Water Demand Forecasting in Water-Stressed Urban Basins Using Recursive Aggregation Models (Haskell Backend with Streamlit Dashboard)

1. System Overview

The system forecasts future water demand in water-stressed urban basins using historical consumption datasets and environmental indicators. The core forecasting logic is implemented in Haskell using recursive aggregation models, while the user interface and visualization layer are implemented using Streamlit.

The architecture combines functional programming for predictive computation with an interactive dashboard for analysis and visualization.

The system processes historical data such as:

total water consumption

rainfall impact

groundwater depletion rate

per capita water use

industrial and agricultural water usage

Using these inputs, the system predicts future water demand through recursive forecasting algorithms.

2. System Architecture

The system follows a three-layer architecture.

Architecture Layers

Data Processing Layer

Forecast Engine (Haskell)

Visualization Layer (Streamlit Dashboard)

Architecture Diagram
Dataset Input (CSV)
        ↓
Data Preprocessing (Python)
        ↓
Feature Aggregation
        ↓
Recursive Forecast Engine (Haskell)
        ↓
Prediction Output (JSON / CSV)
        ↓
Streamlit Dashboard
        ↓
Visualization & Scenario Analysis

The Haskell module acts as the forecasting engine, while the Streamlit application serves as the user interface.

3. System Components
3.1 Data Input Module

The data input module reads historical water demand datasets and prepares them for preprocessing.

Responsibilities

reading CSV datasets

validating dataset structure

preparing input data for processing

Expected Dataset Attributes
Attribute	Description
Country	Region or country
Year	Year of record
Total Water Consumption	Total demand value
Per Capita Water Use	Average individual consumption
Agricultural Water Use	Agricultural sector usage
Industrial Water Use	Industrial sector usage
Rainfall Impact	Rainfall influence
Groundwater Depletion Rate	Groundwater extraction indicator
Water Scarcity Level	Water stress classification
3.2 Data Preprocessing Module

The preprocessing module prepares the dataset for forecasting.

Processing Tasks

cleaning column names

handling missing values

normalizing numeric features

generating lag features

encoding categorical variables

Example Lag Feature
LagDemand(t-1) = WaterDemand from previous year

Lag features allow the recursive forecasting model to capture temporal demand patterns.

3.3 Feature Aggregation Module

The feature aggregation module combines environmental variables into an aggregated demand factor.

Aggregation Model
AggregatedFactor =
w1 × PerCapitaWaterUse
+ w2 × RainfallImpact
+ w3 × GroundwaterDepletionRate
+ w4 × AgriculturalWaterUse

Where:

w1, w2, w3, w4 are weighting coefficients.

The aggregated factor represents the environmental pressure influencing water demand.

3.4 Haskell Forecast Engine

The forecasting engine is implemented in Haskell using recursive functions.

Purpose

perform recursive demand forecasting

compute future demand values

process aggregated features

Haskell is used to demonstrate functional programming concepts including:

recursion

immutable data structures

pure functions

declarative modeling

4. Haskell Forecast Module Design
Data Structure

Water demand records are represented using structured data types.

Example conceptual representation:

WaterRecord
{
    year
    consumption
    rainfallImpact
    groundwaterRate
    scarcityLevel
}

Each record represents water demand for a specific time period.

Recursive Forecast Function

The forecasting algorithm calculates demand recursively.

Conceptual formula:

Demand(t) =
α × Demand(t−1)
+ β × AggregatedFactor(t)

Where:

Demand(t) is predicted demand

Demand(t−1) is previous demand

AggregatedFactor(t) represents environmental influence

Recursive Prediction Process
Year1 → Historical Demand
Year2 → Prediction using Year1
Year3 → Prediction using Year2
Year4 → Prediction using Year3

Each predicted value becomes the input for the next step.

5. Python Integration Layer

Python acts as the integration layer between the dataset and the Haskell forecasting engine.

Responsibilities

preprocessing the dataset

preparing aggregated features

calling the Haskell forecasting program

collecting prediction results

The Python layer sends input data to the Haskell module and retrieves forecast results.

6. Streamlit Dashboard

The Streamlit dashboard provides the user interface for interacting with the forecasting system.

Dashboard Functions

dataset upload

parameter adjustment

forecast execution

result visualization

Dashboard Components
Component	Description
Dataset Upload	Upload water consumption dataset
Forecast Controls	Adjust forecasting parameters
Prediction Graph	Display forecast trends
Results Table	Show predicted demand values
Evaluation Metrics	Display MAE and RMSE
7. Model Evaluation Module

The evaluation module measures forecasting accuracy.

Metrics
Mean Absolute Error (MAE)
MAE = (1/n) Σ |Actual − Predicted|
Root Mean Square Error (RMSE)
RMSE = sqrt((1/n) Σ (Actual − Predicted)²)

These metrics measure the difference between predicted and actual values.

8. Data Flow

The system processes forecasting tasks through the following pipeline:

Dataset Upload
        ↓
Data Preprocessing
        ↓
Feature Aggregation
        ↓
Haskell Recursive Forecast Engine
        ↓
Prediction Output
        ↓
Evaluation Metrics
        ↓
Visualization Dashboard
9. Algorithm Design
Recursive Forecast Algorithm
1 Load dataset
2 Preprocess dataset
3 Compute aggregated feature score
4 Initialize previous demand value
5 For each future year:
       compute new demand using recursive formula
       store predicted demand
6 Return prediction results
10. Performance Considerations
Efficiency

Recursive computations should remain efficient even for large time-series datasets.

Memory Usage

Haskell’s immutable data structures ensure safe and predictable computations.

Scalability

The system allows additional variables such as population growth or climate indicators to be added without modifying the recursive structure.

11. System Limitations

The system may face limitations such as:

dependency on dataset quality

propagation of recursive prediction errors

inability to capture sudden environmental disruptions

12. Future Enhancements

Possible improvements include:

integrating real-time water consumption data

implementing machine learning forecasting models

adding GIS-based basin visualization

developing a fully web-based water demand analytics platform