import streamlit as st
import pandas as pd
import subprocess
import json
import os
import plotly.express as px
import plotly.graph_objects as go
import joblib
import numpy as np

st.set_page_config(page_title="Water Demand Forecaster", layout="wide")

st.title("🌊 Projected Water Demand Forecasting")
st.markdown("Forecast future water demands based on custom scenarios using a recursive Haskell analytics engine.")

st.sidebar.header("Scenario Configuration")
st.sidebar.markdown("Set the initial parameters for the starting year.")

population = st.sidebar.number_input("Population Indicator (Normalized)", value=0.5, step=0.01)
industrial_pct = st.sidebar.number_input("Industrial Water Use (%)", value=0.4, step=0.01)
agricultural_pct = st.sidebar.number_input("Agricultural Water Use (%)", value=0.3, step=0.01)
water_scarcity = st.sidebar.number_input("Water Scarcity Level", value=0.6, step=0.01)

st.sidebar.markdown("---")
st.sidebar.markdown("**Historical Lags**")
lag_1 = st.sidebar.number_input("Demand (T-1)", value=0.5, step=0.01)
lag_2 = st.sidebar.number_input("Demand (T-2)", value=0.45, step=0.01)
n_steps = st.sidebar.slider("Forecast Horizon (Years)", min_value=1, max_value=20, value=10)

@st.cache_resource
def load_rf_model(base_dir):
    model_path = os.path.join(base_dir, 'output', 'rf_model.joblib')
    max_vals_path = os.path.join(base_dir, 'output', 'feature_max_vals.json')
    if os.path.exists(model_path) and os.path.exists(max_vals_path):
        model = joblib.load(model_path)
        with open(max_vals_path, 'r') as f:
            max_vals = json.load(f)
        return model, max_vals
    return None, None

if st.sidebar.button("Run Forecast"):
    with st.spinner("Processing scenario through Haskell forecasting engine..."):
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        haskell_exe = os.path.join(base_dir, 'haskell', 'ForecastEngine.exe')
        
        if not os.path.exists(haskell_exe):
            haskell_exe = os.path.join(base_dir, 'haskell', 'ForecastEngine')
            
        if not os.path.exists(haskell_exe):
            st.error("ForecastEngine executable not found. Please compile the Haskell engine using `ghc`.")
            st.stop()
            
        args = [
            str(haskell_exe),
            str(n_steps),
            str(population),
            str(industrial_pct),
            str(agricultural_pct),
            str(water_scarcity),
            str(lag_1),
            str(lag_2)
        ]
        
        try:
            result = subprocess.run(args, capture_output=True, text=True, check=True)
            output = result.stdout.strip()
            predictions = json.loads(output)
            
            data = []
            for i, p in enumerate(predictions):
                p['year'] = f"Year {i+1}"
                data.append(p)
                
            df = pd.DataFrame(data)
            
            st.success("Forecast generated successfully!")
            
            # Predict using Random Forest
            rf_model, rf_max_vals = load_rf_model(base_dir)
            if rf_model is not None:
                rf_predictions = []
                cur_pop = population * rf_max_vals.get('per_capita_water_use_l_per_day', 100)
                cur_ind = industrial_pct * rf_max_vals.get('industrial_water_use_percent', 100)
                # Map agricultural use backwards if needed, or straight
                cur_agr = agricultural_pct * rf_max_vals.get('agricultural_water_use_percent', 100)
                cur_scar = water_scarcity * rf_max_vals.get('water_scarcity_level', 2.0)
                cur_l1 = lag_1 * rf_max_vals.get('lag_1', 1)
                cur_l2 = lag_2 * rf_max_vals.get('lag_2', 1)
                
                for _ in range(n_steps):
                    X = pd.DataFrame([{
                        'per_capita_water_use_l_per_day': cur_pop,
                        'industrial_water_use_percent': cur_ind,
                        'agricultural_water_use_percent': cur_agr,
                        'water_scarcity_level': cur_scar,
                        'lag_1': cur_l1,
                        'lag_2': cur_l2
                    }])
                    pred = rf_model.predict(X)[0]
                    rf_predictions.append(pred)
                    
                    cur_l2 = cur_l1
                    cur_l1 = pred
                    cur_pop *= 1.01
                    cur_ind *= 1.015
                    cur_agr *= 0.99
                    cur_scar = min(rf_max_vals.get('water_scarcity_level', 2.0), cur_scar + (pred * 0.02 * (rf_max_vals.get('water_scarcity_level', 2.0)/100)))

                df['rf_demand_raw'] = rf_predictions
                
                # Normalize RF predictions dynamically to compare trajectory directly against Haskell's 0-1 scale
                min_rf = min(rf_predictions)
                max_rf = max(rf_predictions)
                h_min = df['demand'].min()
                h_max = df['demand'].max()
                if max_rf > min_rf:
                    df['rf_demand_normalized'] = [(x - min_rf) / (max_rf - min_rf) * (h_max - h_min) + h_min for x in rf_predictions]
                else:
                    df['rf_demand_normalized'] = h_max
            

            
            # Key Metrics
            col1, col2, col3 = st.columns(3)
            with col1:
                initial_d = df.iloc[0]['demand']
                final_d = df.iloc[-1]['demand']
                st.metric("Final Year Demand", f"{final_d:.4f}", f"{(final_d - initial_d)/initial_d * 100:.1f}%")
            with col2:
                st.metric("Final Scarcity Level", f"{df.iloc[-1]['scarcity']:.4f}")
            with col3:
                avg_demand = df['demand'].mean()
                st.metric("Average Demand", f"{avg_demand:.4f}")
                
            st.markdown("---")
            
            # Main chart visually comparing Haskell vs Random Forest
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=df['year'], y=df['demand'], mode='lines+markers', name='Haskell Engine',
                                     line=dict(color='#007ACC', width=3), marker=dict(size=8)))
            if 'rf_demand_normalized' in df.columns:
                fig.add_trace(go.Scatter(x=df['year'], y=df['rf_demand_normalized'], mode='lines+markers', line=dict(dash='dash', color='#FF4B4B', width=3),
                                         name='Random Forest ML (Normalized Trajectory)', marker=dict(size=8, symbol='diamond')))
                                         
            fig.update_layout(title=f"{n_steps}-Year Projected Water Demand: Haskell Analytics vs ML Pipeline",
                              yaxis_title="Aggregated Demand Score (Normalized)",
                              legend=dict(yanchor="top", y=0.99, xanchor="left", x=0.01),
                              hovermode="x unified")
            st.plotly_chart(fig, use_container_width=True)
            
            # Secondary row
            col_chart, col_data = st.columns([1.5, 1])
            with col_chart:
                fig_comp = px.line(df, x='year', y=['population', 'industrial', 'agricultural', 'scarcity'], 
                                        title="Changes in Environmental/State Indicators")
                fig_comp.update_layout(yaxis_title="Normalized Values", legend_title="Components")
                st.plotly_chart(fig_comp, use_container_width=True)
            with col_data:
                st.markdown("### Raw Forecast Data")
                st.dataframe(df.style.highlight_max(axis=0))
                
        except subprocess.CalledProcessError as e:
            st.error(f"Error running Haskell engine. Make sure inputs are correct.\\nError: {e.stderr}")
        except json.JSONDecodeError:
            st.error(f"Error decoding output from Haskell engine.\\nRaw Output: {output}")

st.markdown("---")
st.markdown("Built with 💧 Streamlit and 🚀 Haskell")
