import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"""
Project: Fleet-Scale Remaining Useful Life (RUL) Prediction
Dataset: NASA CMAPSS (Turbofan Engine Degradation)
Description: Data loading, RUL calculation, and sensor degradation visualization.
"""

# 1. Define column names based on NASA documentation
col_names = ['unit', 'cycles', 'setting1', 'setting2', 'setting3']
col_names += [f's{i}' for i in range(1, 22)]

# 2. Load the training data 
# Using a raw string (r'') for the separator and the correct relative path
try:
    data_path = '01_Predictive_Maintenance_RUL/CMAPSSData/train_FD001.txt'
    df = pd.read_csv(data_path, sep=r'\s+', header=None, names=col_names)
    print(f"Successfully loaded: {data_path}")
    print(f"Dataset dimensions: {df.shape[0]} rows and {df.shape[1]} columns.")
except FileNotFoundError:
    print("Error: 'train_FD001.txt' not found. Please check your folder structure.")

# 3. Calculate Remaining Useful Life (RUL)
# Finding the maximum cycle reached by each unit before failure
max_cycles = df.groupby('unit')['cycles'].max().reset_index()
max_cycles.columns = ['unit', 'max_cycle']

# Merging data and computing RUL (distance to failure)
df = df.merge(max_cycles, on='unit', how='left')
df['RUL'] = df['max_cycle'] - df['cycles']

# 4. Data Visualization - Reliability Engineering Perspective
# Analyzing Unit 1 as a sample for sensor drift monitoring
sample_unit = 1
unit_data = df[df['unit'] == sample_unit]

plt.figure(figsize=(12, 6))

# Sensors 11 and 12 typically show clear degradation patterns in this dataset
plt.plot(unit_data['cycles'], unit_data['s11'], label='Sensor 11 (LPC Outlet Temp)', color='blue', alpha=0.7)
plt.plot(unit_data['cycles'], unit_data['s12'], label='Sensor 12 (HPC Outlet Temp)', color='red', alpha=0.7)

# Visualizing the end-of-life point
plt.axvline(x=unit_data['cycles'].max(), color='black', linestyle='--', label='Critical Failure Point')

plt.title(f'Industrial Sensor Degradation Trend - Asset Unit {sample_unit}', fontsize=14)
plt.xlabel('Operational Cycles (Time)', fontsize=12)
plt.ylabel('Normalized Signal Reading', fontsize=12)
plt.legend(loc='best')
plt.grid(True, linestyle=':', alpha=0.6)

# Display the plot
plt.tight_layout()
plt.show()

# 5. Output summary for verification
print("\nSample RUL Calculation (First 5 records):")
print(df[['unit', 'cycles', 'RUL']].head())