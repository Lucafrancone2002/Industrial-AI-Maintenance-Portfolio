import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# 1. Define column names (based on NASA documentation)
col_names = ['unit', 'cycles', 'setting1', 'setting2', 'setting3']
col_names += [f's{i}' for i in range(1, 22)]

# 2. Load the training data
# Ensure 'train_FD001.txt' is in the same folder as this script
df = pd.read_csv('train_FD001.txt', sep='\s+', header=None, names=col_names)

print(f"Dataset loaded: {df.shape[0]} rows and {df.shape[1]} columns.")

# 3. Calculate Remaining Useful Life (RUL)
# For each unit, we find the maximum cycle reached before failure
max_cycles = df.groupby('unit')['cycles'].max().reset_index()
max_cycles.columns = ['unit', 'max_cycle']

# Merge back and calculate RUL for each row
df = df.merge(max_cycles, on='unit', how='left')
df['RUL'] = df['max_cycle'] - df['cycles']

# 4. Data Visualization - Sensor Trend Analysis
# We choose Unit 1 as a sample to see how sensor values change
sample_unit = 1
unit_data = df[df['unit'] == sample_unit]

plt.figure(figsize=(12, 6))
# Sensor 11 and 12 often show clear degradation in this dataset
plt.plot(unit_data['cycles'], unit_data['s11'], label='Sensor 11', color='blue')
plt.plot(unit_data['cycles'], unit_data['s12'], label='Sensor 12', color='red')

plt.axvline(x=unit_data['cycles'].max(), color='black', linestyle='--', label='Point of Failure')
plt.title(f'Sensor Degradation Trend - Unit {sample_unit} (KLA-Style Reliability Analysis)')
plt.xlabel('Operation Cycles')
plt.ylabel('Sensor Readings (Normalized)')
plt.legend()
plt.grid(True)
plt.show()

# 5. Exporting a summary for GitHub
print("Sample RUL calculation (First 5 rows):")
print(df[['unit', 'cycles', 'RUL']].head())