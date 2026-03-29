"""
=========================================================
Global River Discharge Fetcher - Narmada River
=========================================================
This script demonstrates how to retrieve simulated, live 
streamflow data for international rivers using the 
Open-Meteo Global Flood API (powered by the GloFAS model).

It fetches the last 30 days of historical data and a 
7-day forecast for the Narmada River.

Libraries required: requests, pandas, matplotlib
"""

import requests
import pandas as pd
import matplotlib.pyplot as plt

print("📡 Connecting to Open-Meteo Flood API for Narmada River...")

# 1. Define the API request parameters
# Coordinates for Narmada River (near Sardar Sarovar Dam)
latitude = 21.8380
longitude = 73.7191

# Build the URL to request daily river discharge data
# We request 30 days of past data and 7 days of forecast
url = f"https://flood-api.open-meteo.com/v1/flood?latitude={latitude}&longitude={longitude}&daily=river_discharge&past_days=30&forecast_days=7"

# 2. Fetch and Parse the Data
response = requests.get(url)
if response.status_code == 200:
    print("✅ Data retrieved successfully!")
    data = response.json()
    
    # Navigate the JSON structure
    dates = data['daily']['time']
    discharge = data['daily']['river_discharge']
    
    # Convert into a clean Pandas DataFrame
    df = pd.DataFrame({'Date': pd.to_datetime(dates), 'Discharge_m3s': discharge})
    
    # 3. Plotting the Real-World Data
    print("📈 Generating hydrograph...")
    plt.figure(figsize=(12, 6))
    
    # Plotting with a vibrant water-blue color
    plt.plot(df['Date'], df['Discharge_m3s'], color='#00C9FF', linewidth=2.5, label='Simulated Discharge')
    plt.fill_between(df['Date'], df['Discharge_m3s'], color='#00C9FF', alpha=0.2)
    
    # Add a vertical line to separate past data from the future forecast
    today = pd.Timestamp.now().normalize()
    plt.axvline(x=today, color='red', linestyle='--', label='Today (Forecast Starts)')

    # Formatting the chart
    plt.title('Narmada River Discharge (GloFAS Model)', fontsize=16, fontweight='bold')
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('Discharge ($m^3/s$)', fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()
    plt.tight_layout()
    
    plt.show()

else:
    print(f"❌ Failed to retrieve data. HTTP Status Code: {response.status_code}")
