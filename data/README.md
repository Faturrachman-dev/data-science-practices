# Dataset Documentation

## Beijing Air Quality Dataset (2013-2017)

### Overview
This dataset contains hourly air quality measurements from the Aotizhongxin monitoring station in Beijing, covering the period from March 2013 to February 2017.

### Data Fields
1. **Temporal Information**:
   - year: Year of measurement
   - month: Month of measurement
   - day: Day of measurement
   - hour: Hour of measurement (0-23)

2. **Air Pollutants**:
   - PM2.5: Fine particulate matter (μg/m³)
   - PM10: Inhalable particles (μg/m³)
   - SO2: Sulfur dioxide (μg/m³)
   - NO2: Nitrogen dioxide (μg/m³)

3. **Weather Conditions**:
   - TEMP: Temperature (°C)
   - PRES: Pressure (hPa)
   - WSPM: Wind speed (m/s)

4. **Derived Fields**:
   - season: Calculated season based on month
   - datetime: Combined date and time field

### Source
UCI Machine Learning Repository 