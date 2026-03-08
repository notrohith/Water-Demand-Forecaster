Design Document
Project Title

Projected Water Demand Forecasting in Water-Stressed Urban Basins Using Recursive Aggregation Models (Haskell Backend with Streamlit Dashboard)

1. Design Overview

The system is designed as an interactive forecasting dashboard that allows users to upload water consumption datasets, run forecasting models, and visualize predicted water demand trends.

The dashboard is built using Streamlit and communicates with the Haskell forecasting engine through a Python integration layer.

The design emphasizes:

minimalistic interface

clean data visualization

modern analytics dashboard layout

interactive forecasting controls

The goal is to create an interface that is easy to use, visually appealing, and suitable for demonstrating forecasting models in academic presentations.

2. Design Principles

The design follows several key principles.

Simplicity

The interface avoids clutter and presents only essential information.

Readability

Graphs, tables, and metrics are clearly displayed with proper spacing and typography.

Interactivity

Users can upload datasets and instantly visualize predictions.

Consistency

All UI components follow consistent styling and layout patterns.

Analytical Focus

The dashboard is designed like a data analytics platform, prioritizing charts and insights over decorative elements.

3. User Interface Layout

The dashboard follows a single-page layout.

Page Layout Structure
--------------------------------------------------
                   HEADER
--------------------------------------------------

              DATASET UPLOAD PANEL

--------------------------------------------------

             FORECAST CONTROL PANEL

--------------------------------------------------

           DEMAND FORECAST VISUALIZATION

--------------------------------------------------

             RESULTS AND METRICS PANEL

--------------------------------------------------

                     FOOTER
--------------------------------------------------

This layout ensures that the most important information (graphs and predictions) appears in the center of the screen.

4. Dashboard Components
4.1 Header Section

The header provides project identification and context.

Elements

Project title

Short description of the forecasting system

Example display:

Projected Water Demand Forecasting Dashboard

Predict future water demand in water-stressed urban regions
using recursive aggregation models implemented in Haskell.
4.2 Dataset Upload Panel

This section allows users to upload historical water consumption datasets.

Components

file upload button

dataset preview table

Example interface:

Upload Dataset
[ Choose CSV File ]

Preview Dataset
----------------------------------
Year | Water Consumption | Rainfall
----------------------------------
2015 | 450 | 900
2016 | 470 | 870

Once uploaded, the dataset is passed to the preprocessing pipeline.

4.3 Forecast Control Panel

The forecast control panel allows users to configure forecasting parameters.

Adjustable Parameters

forecast horizon (number of future years)

rainfall adjustment

groundwater depletion rate

per capita consumption change

Example interface:

Forecast Horizon: 5 Years

Rainfall Impact Adjustment: -10%
Groundwater Depletion Increase: +5%
Per Capita Consumption Growth: +2%

These parameters influence the aggregated demand score used in the recursive model.

4.4 Forecast Visualization Panel

This is the central component of the dashboard.

The panel displays graphs showing historical and predicted water demand trends.

Visualization Types

Historical demand trend

Forecast demand trend

Combined historical vs predicted demand

Example visualization:

Water Demand Forecast (2010–2035)

Historical Demand ───────────
Predicted Demand  ─ ─ ─ ─ ─

Graphs are interactive and allow:

zooming

hover data inspection

time range exploration

4.5 Results Table

Below the graph, the system displays prediction results in tabular form.

Example table:

Year	Predicted Water Demand
2026	520
2027	540
2028	558

This allows users to inspect exact forecast values.

4.6 Model Evaluation Metrics

The system displays forecasting accuracy metrics.

Example metrics:

Model Performance

MAE  : 12.4
RMSE : 15.7

Metrics are shown in card-style panels for visual clarity.

4.7 Scenario Simulation Panel

Users can test different environmental scenarios.

Example:

Scenario Simulation

Rainfall Decrease → Higher Demand
Groundwater Depletion → Increased Demand
Lower Population Growth → Reduced Demand

When parameters change, the forecast graph updates dynamically.

5. Visual Design

The dashboard uses a clean analytics-style design.

Color Palette
Element	Color
Primary	Deep Blue
Accent	Teal
Background	Light Gray
Card Panels	White
Text	Dark Gray

These colors convey a water-related theme while maintaining readability.

6. Typography

Readable modern typography is used.

Element	Style
Headings	Bold Sans-serif
Body Text	Regular Sans-serif
Metrics	Semi-bold numeric

Consistent font sizes ensure readability across the dashboard.

7. UI Component Layout

The interface uses card-based components to separate sections.

Example layout:

--------------------------------
| Dataset Upload               |
--------------------------------

--------------------------------
| Forecast Controls            |
--------------------------------

--------------------------------
| Demand Forecast Graph        |
--------------------------------

--------------------------------
| Prediction Results Table     |
--------------------------------

--------------------------------
| Model Evaluation Metrics     |
--------------------------------

Card layouts improve organization and visual clarity.

8. Dynamic Behavior

The system updates dynamically in response to user actions.

Dynamic Features

dataset preview updates after upload

forecast recalculates when parameters change

graphs update instantly after model execution

metrics refresh after predictions are generated

This interactivity improves user experience.

9. User Interaction Flow

The system interaction sequence is:

User opens dashboard
        ↓
User uploads dataset
        ↓
System preprocesses data
        ↓
User configures forecast parameters
        ↓
Haskell forecasting engine runs
        ↓
Predictions returned to dashboard
        ↓
Graphs and results displayed
10. Accessibility Considerations

The interface ensures accessibility through:

high contrast colors

readable font sizes

simple navigation layout

clearly labeled controls

These features make the dashboard usable for a wide range of users.

11. Final Design Characteristics

The final system interface has the following qualities:

minimalistic design

clean analytics dashboard layout

dynamic forecasting visualization

interactive parameter controls

clear presentation of predictions and metrics

The design ensures the project appears professional, visually appealing, and suitable for academic demonstration while effectively communicating water demand forecasting insights.