"""
=========================================================
Hydrograph Plotter - Starter Template
=========================================================
This script demonstrates how to plot a standard streamflow 
hydrograph using Python. It generates synthetic storm data 
so you can test the visualisation immediately.

Libraries required: pandas, matplotlib, numpy
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

print("Generating synthetic hydrological data...")

# 1. Generate Sample Data (Time vs. Discharge)
# Creating a 10-day period with hourly intervals
dates = pd.date_range(start="2026-06-01", periods=240, freq="h")

# Simulating a rain event: baseflow + a peak storm curve 
baseflow = 15.0 # cubic meters per second (cms)
storm_flow = 120 * np.exp(-0.04 * np.arange(240)) * np.sin(np.linspace(0, 3.5, 240))**2
discharge = baseflow + storm_flow

# Create a DataFrame to hold our data cleanly
df = pd.DataFrame({'Datetime': dates, 'Discharge_cms': discharge})

# 2. Plotting the Hydrograph
print("Plotting hydrograph...")
plt.figure(figsize=(12, 6))

# Plot the main discharge line and fill the area underneath
plt.plot(df['Datetime'], df['Discharge_cms'], color='#0055ff', linewidth=2.5, label='Total Streamflow (cms)')
plt.fill_between(df['Datetime'], df['Discharge_cms'], baseflow, color='#00C9FF', alpha=0.3)

# Add a dashed line for baseflow
plt.axhline(y=baseflow, color='gray', linestyle='--', linewidth=1.5, label='Baseflow')

# Formatting the chart for a professional engineering look
plt.title('Synthetic Streamflow Hydrograph', fontsize=16, fontweight='bold')
plt.xlabel('Date / Time', fontsize=12)
plt.ylabel('Discharge ($m^3/s$)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(loc='upper right', fontsize=11)
plt.tight_layout()

# Display the plot
plt.show()
