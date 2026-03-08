Product Requirements Document (PRD)
Project Title

Projected Water Demand Forecasting in Water-Stressed Urban Basins Using Recursive Aggregation Models (Haskell Forecast Engine with Streamlit Dashboard)

1. Introduction

Urban regions facing water scarcity require accurate forecasting tools to plan sustainable water resource management. Increasing population, climate variability, groundwater depletion, and industrial expansion significantly influence water demand patterns.

This project proposes a water demand forecasting system using recursive aggregation models implemented in Haskell, combined with an interactive Streamlit dashboard for visualization and analysis.

The Haskell backend performs the computational forecasting logic using recursive functions and functional programming principles. The Streamlit interface provides an intuitive platform for users to upload datasets, run forecasts, and visualize predicted water demand trends.

The system aims to demonstrate how functional programming (Haskell) can be applied to predictive modeling in water resource management, while offering a modern analytical interface for exploring forecasting results.

2. Problem Statement

Water-stressed urban basins require reliable forecasting systems to anticipate future water demand and support effective infrastructure planning.

Traditional forecasting systems often suffer from:

static prediction models

limited adaptability to environmental changes

lack of interactive analysis tools

Without accurate forecasting systems, urban planners face challenges such as inefficient water allocation, infrastructure stress, and unsustainable groundwater extraction.

This project addresses these challenges by implementing a recursive forecasting model in Haskell, combined with an interactive visualization dashboard, enabling users to analyze future demand scenarios and understand how environmental factors influence water consumption.

3. Objectives

The primary objectives of the project are:

Implement a water demand forecasting model in Haskell

Apply recursive aggregation techniques for demand prediction

Analyze the impact of environmental variables on water demand

Build an interactive Streamlit dashboard for visualizing forecasting results

Enable users to simulate different water demand scenarios

Evaluate forecasting performance using statistical metrics

4. Scope of the Project

The system focuses on predicting future water demand trends based on historical datasets and environmental indicators.

The scope includes:

preprocessing water consumption datasets

aggregating environmental and consumption variables

implementing recursive forecasting logic in Haskell

generating multi-year demand projections

visualizing results through a Streamlit dashboard

evaluating model accuracy

The project does not include real-time sensor integration or direct water infrastructure control, as it focuses on predictive modeling and analytical visualization.

5. System Overview

The system consists of three major components:

Data Processing Layer

Haskell Forecast Engine

Streamlit Visualization Dashboard

The Haskell forecasting engine serves as the core computational component of the system.

System Workflow
Dataset Input
      ↓
Data Preprocessing (Python)
      ↓
Feature Aggregation
      ↓
Recursive Forecast Model (Haskell)
      ↓
Prediction Output
      ↓
Streamlit Dashboard Visualization

The Streamlit dashboard interacts with the Haskell backend to display predictions and demand trends.

6. Functional Requirements
FR1: Dataset Upload

The system must allow users to upload historical water demand datasets through the dashboard interface.

Typical dataset attributes include:

Year

Total Water Consumption

Per Capita Water Use

Agricultural Water Use

Industrial Water Use

Rainfall Impact

Groundwater Depletion Rate

Water Scarcity Level

FR2: Data Preprocessing

The system must preprocess input datasets before forecasting.

Processing tasks include:

cleaning column names

handling missing values

generating lag features

normalizing variables

preparing input features for forecasting

FR3: Feature Aggregation

Environmental and demand variables must be combined to produce an aggregated demand score.

Example:

DemandScore =
w1 × PerCapitaWaterUse
+ w2 × RainfallImpact
+ w3 × GroundwaterDepletionRate
+ w4 × AgriculturalWaterUse

This aggregated score is used as an input to the recursive forecasting model.

FR4: Recursive Forecast Model (Haskell)

The forecasting model must be implemented using recursive functions in Haskell.

Forecast formula:

Demand(t) =
α × Demand(t−1)
+ β × AggregatedFactors(t)

Each predicted value becomes the input for the next time step.

FR5: Scenario Simulation

Users must be able to simulate demand scenarios by modifying variables such as:

rainfall levels

groundwater depletion rates

per capita water consumption

The system should recompute forecasts dynamically.

FR6: Visualization Dashboard

The Streamlit dashboard must display:

historical water demand trends

predicted demand trends

comparison between historical and forecast values

model evaluation metrics

The dashboard should allow interactive exploration of the dataset.

FR7: Prediction Output

The system must generate predicted demand values for future years.

Example:

Year	Predicted Water Demand
2026	520
2027	540
2028	558

Predictions must be displayed both as tables and graphs.

FR8: Model Evaluation

The system must calculate forecasting accuracy using metrics such as:

Mean Absolute Error (MAE)

Root Mean Square Error (RMSE)

These metrics help assess the reliability of the forecasting model.

7. Non-Functional Requirements
Performance

The system should process datasets efficiently and generate predictions within a few seconds.

Usability

The Streamlit dashboard must provide a clean, minimalistic interface for interacting with forecasting results.

Scalability

The forecasting system should support additional environmental variables without major changes to the core algorithm.

Maintainability

The codebase must follow modular architecture with separate components for preprocessing, forecasting, and visualization.

8. System Workflow
Dataset Upload
      ↓
Data Cleaning and Preprocessing
      ↓
Feature Aggregation
      ↓
Recursive Forecast Model (Haskell)
      ↓
Prediction Generation
      ↓
Visualization and Analysis (Streamlit)
9. Expected Outputs

The system will generate:

predicted water demand values for future years

visual graphs of historical and forecast demand

comparison between predicted and historical demand

evaluation metrics measuring model accuracy

These outputs help demonstrate how water demand may evolve in water-stressed urban basins.

10. Success Criteria

The project will be considered successful if:

the recursive forecasting algorithm implemented in Haskell generates consistent predictions

the Streamlit dashboard clearly visualizes demand trends

environmental variables influence demand predictions meaningfully

the system demonstrates how functional programming can be used for predictive analytics