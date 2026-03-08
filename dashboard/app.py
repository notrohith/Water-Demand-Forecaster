import streamlit as st
import pandas as pd
import subprocess
import json
import os
import plotly.express as px

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
            
            # Main chart
            fig = px.line(df, x='year', y='demand', markers=True, title=f"{n_steps}-Year Projected Water Demand")
            fig.update_traces(line_color='#007ACC', marker=dict(size=8, color='#005A9E'))
            fig.update_layout(yaxis_title="Aggregated Demand Score")
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
