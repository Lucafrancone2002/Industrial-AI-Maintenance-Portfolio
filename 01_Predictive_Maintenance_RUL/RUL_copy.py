"""
Project: Fleet-Scale Remaining Useful Life (RUL) Prediction
Author: Luca Francone
Description: This script performs Exploratory Data Analysis (EDA) on the NASA CMAPSS dataset 
             to identify degradation patterns in industrial sensors.
"""

import pandas as pd
import matplotlib.pyplot as plt

# Load dataset with predefined column names
# Note: Data source is NASA Ames Prognostics Data Repository
col_names = ['unit', 'cycles', 'setting1', 'setting2', 'setting3'] + [f's{i}' for i in range(1, 22)]
# Use the correct relative path to the data file
df = pd.read_csv('01_Predictive_Maintenance_RUL/CMAPSSData/train_FD001.txt', sep=r'\s+', header=None, names=col_names)


# Displaying sensor health trends to identify early signs of hardware fatigue
plt.figure(figsize=(10, 6))
plt.plot(df[df['unit']==1]['cycles'], df[df['unit']==1]['s11'], color='navy')
plt.title('Sensor Signal Drift - Hardware Degradation Monitoring')
plt.xlabel('Operational Cycles')
plt.ylabel('Normalized Signal Value')
plt.grid(True)
plt.show()

