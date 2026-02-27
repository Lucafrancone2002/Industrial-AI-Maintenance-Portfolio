import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

"""
Project: Industrial Reliability & Predictive Maintenance Analysis
Dataset: NASA CMAPSS (Turbofan Engine Degradation)
Author: Luca Francone
Description: This script performs automated data ingestion, Remaining Useful Life (RUL) 
             calculation, and statistical sensor correlation to identify 
             degradation patterns in high-tech industrial equipment.
"""

# 1. Configuration and Data Ingestion
# Defining sensor names based on the official NASA documentation
col_names = ['unit', 'cycles', 'setting1', 'setting2', 'setting3'] + [f's{i}' for i in range(1, 22)]
path = '01_Predictive_Maintenance_RUL/CMAPSSData/train_FD001.txt'

try:
    # Using raw string for regex separator to avoid SyntaxWarnings (Python 3.12+)
    df = pd.read_csv(path, sep=r'\s+', header=None, names=col_names)
    print(f"[INFO] Dataset loaded successfully from {path}")
    print(f"[INFO] Total records: {df.shape[0]} | Sensors monitored: 21")
except FileNotFoundError:
    print(f"[ERROR] File not found. Please verify the path: {path}")
    exit()

# 2. Target Engineering: Calculating Remaining Useful Life (RUL)
# We determine the "End-of-Life" (EOL) for each unit to compute the RUL target
max_cycles = df.groupby('unit')['cycles'].max().reset_index()
max_cycles.columns = ['unit', 'max_cycle']

# Merging and calculating RUL (distance to failure in cycles)
df = df.merge(max_cycles, on='unit', how='left')
df['RUL'] = df['max_cycle'] - df['cycles']

# 3. Feature Selection: Statistical Correlation Analysis
# We analyze how each sensor correlates with the RUL to identify predictive features
# High positive/negative correlation indicates a strong degradation signal
df_numeric = df.drop(columns=['unit'])
correlations = df_numeric.corr()['RUL'].sort_values(ascending=False)

print("\n--- Top Sensor Correlations with Asset Degradation ---")
print(correlations.head(5))  # Strong positive correlation (signals decreasing over time)
print(correlations.tail(5))  # Strong negative correlation (signals increasing over time)

# 4. Multi-Plot Visualization
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))

# --- Plot A: Time-Series Sensor Drift ---
# Visualizing Unit 1 as a case study for equipment wear
sample_unit = 1
unit_data = df[df['unit'] == sample_unit]

ax1.plot(unit_data['cycles'], unit_data['s11'], label='Sensor 11 (Physical Drift)', color='blue', alpha=0.8)
ax1.plot(unit_data['cycles'], unit_data['s12'], label='Sensor 12 (Thermal Stress)', color='red', alpha=0.8)
ax1.axvline(x=unit_data['cycles'].max(), color='black', linestyle='--', label='Critical Failure Point')

ax1.set_title(f'Equipment Health Monitoring - Asset Unit {sample_unit}', fontsize=14)
ax1.set_xlabel('Operational Cycles')
ax1.set_ylabel('Normalized Signal')
ax1.legend()
ax1.grid(True, linestyle=':', alpha=0.5)

# --- Plot B: Feature Interaction Heatmap ---
# Selecting the top 10 most relevant sensors for clarity
top_features = correlations.index[:5].tolist() + correlations.index[-5:].tolist()
sns.heatmap(df[top_features].corr(), annot=True, cmap='coolwarm', ax=ax2, fmt=".2f", linewidths=.5)

ax2.set_title('Sensor Correlation Matrix (Feature Selection Strategy)', fontsize=14)

plt.tight_layout()
plt.show()

# 5. Exporting Metadata for Documentation
# Useful for creating summary tables in the README or Technical Abstract
print("\n[INFO] Data processing complete. Ready for model training phase.")

