Technology Stack Document
Project Title

Projected Water Demand Forecasting in Water-Stressed Urban Basins Using Recursive Aggregation Models (Haskell Backend with Streamlit Dashboard)

1. Overview

The system requires technologies capable of performing data preprocessing, recursive forecasting computation, and interactive visualization.

The technology stack is designed around three major layers:

Data Processing Layer

Forecasting Engine

Visualization Dashboard

The forecasting model is implemented using Haskell, while the user interface is built using Streamlit, enabling a clean and interactive analytical dashboard.

2. Programming Languages
Haskell

Haskell is used as the core forecasting engine.

Purpose

implement recursive aggregation forecasting model

process aggregated water demand features

compute future demand predictions

Advantages

functional programming paradigm

strong type safety

recursion-friendly design

pure functions reduce side effects

suitable for modeling mathematical algorithms

Role in System

Haskell performs the core demand prediction calculations.

Python

Python is used as the integration and data processing layer.

Purpose

preprocess dataset

prepare input features for forecasting

call the Haskell forecasting module

process prediction outputs

support the Streamlit dashboard

Advantages

strong ecosystem for data analysis

easy integration with external systems

efficient data manipulation libraries

3. Data Processing Libraries
Pandas

Pandas is used for handling structured datasets.

Responsibilities

loading CSV datasets

cleaning column names

handling missing values

generating lag features

transforming dataset structure

Benefits

efficient tabular data processing

built-in statistical functions

flexible data transformation capabilities

NumPy

NumPy supports numerical computations.

Responsibilities

numerical operations

mathematical transformations

efficient array manipulation

Benefits

optimized numerical calculations

improved performance for large datasets

4. Forecasting Engine
Haskell Recursive Aggregation Model

The forecasting model is implemented in Haskell using recursive functions.

Purpose

predict future water demand

compute recursive demand values

process aggregated environmental variables

Forecast Formula
Demand(t) =
α × Demand(t−1)
+ β × AggregatedFactors(t)

Where:

Demand(t) = predicted water demand

Demand(t−1) = previous demand

AggregatedFactors = environmental indicators

5. Visualization Layer
Streamlit

Streamlit is used to build the interactive dashboard interface.

Purpose

allow dataset upload

display prediction results

visualize demand trends

show evaluation metrics

Features

interactive charts

real-time data updates

simple web application deployment

6. Visualization Libraries
Plotly

Plotly is used to generate interactive graphs.

Responsibilities

plot historical demand trends

display predicted demand curves

visualize forecast comparisons

Features

interactive charts

zooming and panning

hover information display

7. Machine Learning Utilities
Scikit-learn

Scikit-learn is used for evaluation and preprocessing support.

Responsibilities

feature scaling

dataset splitting

performance evaluation

Evaluation Metrics

Mean Absolute Error (MAE)

Root Mean Square Error (RMSE)

8. Data Storage
CSV Dataset Files

The system uses CSV files for storing datasets and prediction results.

Advantages

easy to read and write

compatible with multiple programming environments

suitable for time-series data

9. Development Environment

The system can be developed using standard development tools that support both Python and Haskell.

Typical environment requirements include:

Python runtime environment

Haskell compiler (GHC)

package manager for dependencies

code editor or integrated development environment

terminal for executing scripts

10. System Integration

The integration between Python and Haskell occurs through a command execution interface.

Integration Workflow
Python preprocessing
        ↓
Call Haskell forecasting engine
        ↓
Haskell computes predictions
        ↓
Return prediction results
        ↓
Streamlit dashboard visualizes output

Python serves as the bridge between the Haskell computation engine and the Streamlit interface.

11. Project Structure

The project is organized into modular components.

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

models/
    forecast_output.csv

requirements.txt

This modular structure separates preprocessing, forecasting, and visualization logic.

12. Deployment Options

The system can be deployed in multiple environments.

Local Deployment

Run the forecasting system locally for testing and demonstration.

Cloud Deployment

Host the Streamlit dashboard on a cloud platform for remote access.

13. Summary

The technology stack combines functional programming with modern data analytics tools to build an effective forecasting system.

Key benefits include:

reliable recursive forecasting using Haskell

efficient data processing with Python

interactive visualization through Streamlit

modular architecture supporting future extensions

This stack ensures that the system remains efficient, maintainable, and suitable for demonstrating predictive analytics in water resource management.