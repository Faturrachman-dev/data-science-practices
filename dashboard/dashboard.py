import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
@st.cache_data
def load_data():
    # Changed path to local dashboard folder
    df = pd.read_csv("PRSA_Data_Aotizhongxin_20130301-20170228.csv")
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

    # Seasonal Analysis
    st.header('Seasonal Pollution Patterns')
    seasonal_pollution = df.groupby('season')[['PM2.5', 'PM10', 'SO2', 'NO2']].mean()

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
    weather_columns = ['TEMP', 'PRES', 'WSPM', 'PM2.5']
    correlations = df[weather_columns].corr()

    fig2, ax2 = plt.subplots(figsize=(10, 6))
    sns.heatmap(correlations, annot=True, cmap='coolwarm', center=0, ax=ax2)
    plt.title('Correlation between Weather Conditions and PM2.5')
    st.pyplot(fig2)

if __name__ == "__main__":
    main() 