import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load data
@st.cache_data
def load_data():
    # Get the absolute path to the data file
    current_dir = os.path.dirname(__file__)
    data_path = os.path.join(current_dir, "PRSA_Data_Aotizhongxin_20130301-20170228.csv")
    
    df = pd.read_csv(data_path)
    df['datetime'] = pd.to_datetime(df[['year', 'month', 'day', 'hour']])
    
    # Add season column
    def get_season(month):
        if month in [12, 1, 2]:
            return 'Winter'
        elif month in [3, 4, 5]:
            return 'Spring'
        elif month in [6, 7, 8]:
            return 'Summer'
        else:
            return 'Fall'
    
    # Add the season column
    df['season'] = df['month'].apply(get_season)
    return df

def main():
    st.title('Beijing Air Quality Analysis Dashboard')
    
    df = load_data()

    # Add more interactive features
    st.sidebar.header('Filters')
    
    # 1. Date Range Filter (already exists)
    date_range = st.sidebar.date_input(
        "Select Date Range",
        [df['datetime'].min().date(), df['datetime'].max().date()]
    )
    
    # 2. Season Filter (already exists)
    selected_season = st.sidebar.multiselect(
        'Select Seasons',
        options=df['season'].unique(),
        default=df['season'].unique()
    )
    
    # 3. Add Station Filter (new)
    selected_station = st.sidebar.selectbox(
        'Select Station',
        options=['All'] + list(df['station'].unique())
    )
    
    # 4. Add Hour Range Slider (new)
    hour_range = st.sidebar.slider(
        'Select Hour Range',
        0, 23, (0, 23)
    )

    # Update filter logic
    mask = (
        (df['datetime'].dt.date >= date_range[0]) & 
        (df['datetime'].dt.date <= date_range[1]) & 
        (df['season'].isin(selected_season)) &
        (df['hour'].between(hour_range[0], hour_range[1]))
    )
    
    if selected_station != 'All':
        mask = mask & (df['station'] == selected_station)
        
    filtered_df = df[mask]

    # Seasonal Analysis
    st.header('Seasonal Pollution Patterns')
    seasonal_pollution = filtered_df.groupby('season')[selected_pollutants].mean()

    fig1, ax1 = plt.subplots(figsize=(12, 6))
    seasonal_pollution.plot(kind='bar', ax=ax1)
    plt.title('Average Pollutant Levels by Season')
    plt.xlabel('Season')
    plt.ylabel('Concentration')
    plt.legend(title='Pollutants')
    plt.xticks(rotation=45)
    st.pyplot(fig1)

    # Weather Correlation
    st.header('Weather and PM2.5 Correlation')
    weather_vars = st.multiselect(
        'Select Weather Variables',
        ['TEMP', 'PRES', 'WSPM'],
        default=['TEMP', 'PRES', 'WSPM']
    )
    
    weather_columns = weather_vars + ['PM2.5']
    correlations = filtered_df[weather_columns].corr()

    fig2, ax2 = plt.subplots(figsize=(10, 6))
    sns.heatmap(correlations, annot=True, cmap='coolwarm', center=0, ax=ax2)
    plt.title('Correlation between Weather Conditions and PM2.5')
    st.pyplot(fig2)

if __name__ == "__main__":
    main() 