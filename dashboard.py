import calendar
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Load data
hour_df = pd.read_csv('./hour.csv')

# Drop unnecessary columns
drop_col = ['instant']
for i in hour_df.columns:
    if i in drop_col:
        hour_df.drop(labels=i, axis=1, inplace=True)

# Rename columns
hour_df.rename(columns={
    'dteday': 'dateday',
    'yr': 'year',
    'mnth': 'month',
    'hr' : 'hour',
    'weathersit': 'weather_cond',
    'temp': 'temparature',
    'hum' : 'humidity',
    'cnt': 'count'
}, inplace=True)

# Create monthly usage dataframe
monthly_usage = hour_df.groupby('month')[['count']].sum().reset_index()
monthly_usage['month'] = monthly_usage['month'].apply(lambda x: calendar.month_name[x])

# Set style seaborn
sns.set(style='dark')

# Streamlit Dashboard
st.title('Dashboard Penyewaan Sepeda')

# Monthly Rentals Plot
st.subheader('Jumlah penyewaan sepeda berdasarkan bulan')
fig_monthly, ax_monthly = plt.subplots(figsize=(13, 9))

sns.barplot(
    x=monthly_usage['month'],
    y=monthly_usage['count'],
    label='count',
    color='tab:purple',
    ax=ax_monthly
)

ax_monthly.set_xlabel(None)
ax_monthly.set_ylabel(None)
ax_monthly.set_title('Monthly Bike Rentals Count')
ax_monthly.legend()

# Display the plot in Streamlit
st.pyplot(fig_monthly)

st.write('Bulan Agustus memiliki jumlah penyewaan sepeda tertinggi yakni mencapai 351194 sedangkan bulan Januari memiliki jumlah penyewaan terendah yakni hanya 134933.')

# Hourly Rentals Plot
st.subheader('Jumlah total sepeda yang disewakan berdasarkan Waktu (Hour)')
fig_hourly, ax_hourly = plt.subplots(figsize=(12, 6))
hour_usage = hour_df.groupby('hour')[['count']].sum().reset_index()

sns.lineplot(
    data=hour_usage,
    x="hour",
    y="count",
    label="hour",
    marker="o",
    ax=ax_hourly
)

ax_hourly.set_xticks(range(24))
ax_hourly.set_title("Hourly Bike Rentals")
ax_hourly.set_xlabel("Hour")
ax_hourly.set_ylabel("Count")
ax_hourly.legend()

# Display the plot in Streamlit
st.pyplot(fig_hourly)
st.write('Jika dilihat berdasarkan jumlah jam (hour) terdapat 336860 pengguna yang menyewa sepeda selama 17 jam sedangkan yang terendah yakni pada angka 4428 yang menyewa sepeda selama 4 jam. Sementara itu pengguna yang menyewa sepeda tidak sampai 1 jam memiliki jumlah pengguna hingga 39130f')

st.caption('Copyright (c) Matsnan Haqqi 2024')