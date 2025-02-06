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
            return 'Musim Dingin'
        elif month in [3, 4, 5]:
            return 'Musim Semi'
        elif month in [6, 7, 8]:
            return 'Musim Panas'
        else:
            return 'Musim Gugur'
    
    # Add the season column
    df['season'] = df['month'].apply(get_season)
    return df

def main():
    st.title('Dashboard Analysis Kualitas Udara Beijing')
    
    df = load_data()

    # Add interactive features
    st.sidebar.header('Filter Data')
    
    # 1. Date Range Filter
    date_range = st.sidebar.date_input(
        "Pilih Rentang Tanggal",
        [df['datetime'].min().date(), df['datetime'].max().date()]
    )
    
    # 2. Season Filter
    selected_season = st.sidebar.multiselect(
        'Pilih Musim',
        options=df['season'].unique(),
        default=df['season'].unique()
    )
    
    # 3. Pollutant Filter
    pollutants = ['PM2.5', 'PM10', 'SO2', 'NO2']
    selected_pollutants = st.sidebar.multiselect(
        'Pilih Jenis Polutan',
        options=pollutants,
        default=pollutants
    )
    
    # 4. Station Filter
    selected_station = st.sidebar.selectbox(
        'Pilih Stasiun',
        options=['Semua'] + list(df['station'].unique())
    )
    
    # 5. Hour Range Slider
    hour_range = st.sidebar.slider(
        'Pilih Rentang Jam',
        0, 23, (0, 23)
    )

    # Update filter logic
    mask = (
        (df['datetime'].dt.date >= date_range[0]) & 
        (df['datetime'].dt.date <= date_range[1]) & 
        (df['season'].isin(selected_season)) &
        (df['hour'].between(hour_range[0], hour_range[1]))
    )
    
    if selected_station != 'Semua':
        mask = mask & (df['station'] == selected_station)
        
    filtered_df = df[mask]

    # Seasonal Analysis
    st.header('Pola Polusi Berdasarkan Musim')
    seasonal_pollution = filtered_df.groupby('season')[selected_pollutants].mean()

    fig1, ax1 = plt.subplots(figsize=(12, 6))
    seasonal_pollution.plot(kind='bar', ax=ax1)
    plt.title('Rata-rata Tingkat Polutan per Musim')
    plt.xlabel('Musim')
    plt.ylabel('Konsentrasi (μg/m³)')
    plt.legend(title='Jenis Polutan')
    plt.xticks(rotation=45)
    st.pyplot(fig1)

    # Weather Correlation
    st.header('Korelasi Cuaca dengan PM2.5')
    weather_vars = st.multiselect(
        'Pilih Variabel Cuaca',
        ['TEMP (Suhu)', 'PRES (Tekanan)', 'WSPM (Kec. Angin)'],
        default=['TEMP (Suhu)', 'PRES (Tekanan)', 'WSPM (Kec. Angin)']
    )
    
    # Convert display names back to column names
    weather_map = {
        'TEMP (Suhu)': 'TEMP',
        'PRES (Tekanan)': 'PRES',
        'WSPM (Kec. Angin)': 'WSPM'
    }
    weather_columns = [weather_map[var] for var in weather_vars] + ['PM2.5']
    correlations = filtered_df[weather_columns].corr()

    fig2, ax2 = plt.subplots(figsize=(10, 6))
    sns.heatmap(correlations, annot=True, cmap='coolwarm', center=0, ax=ax2)
    plt.title('Korelasi antara Kondisi Cuaca dan PM2.5')
    st.pyplot(fig2)

if __name__ == "__main__":
    main() 