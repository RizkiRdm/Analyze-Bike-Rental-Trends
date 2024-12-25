import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import plotly.express as px
# helper function : increase/deacrese rent bike function
def percent_rent_bike(df):
    
    holiday_rentals = df[df["holiday_x"] == 1]['cnt_x'].sum()
    workingday_rentals = df[df["workingday_x"] == 1]['cnt_x'].sum()
    total_rentals = df['cnt_x'].sum()
    
    if total_rentals == 0:
        return 0, 0

    # Hitung persentase
    holiday_percentage = (holiday_rentals / total_rentals) * 100
    workingday_percentage = (workingday_rentals / total_rentals) * 100
    
    return holiday_percentage, workingday_percentage
    
    # weekday_avg = df[df["workingday_x"] == 1]["cnt_x"].mean()
    # weekend_avg = df[df["workingday_x"] == 0]["cnt_x"].mean()
    # increase_percentage = ((weekend_avg - weekday_avg) / weekday_avg) * 100 if weekday_avg != 0 else 0
    # return weekday_avg, weekend_avg, increase_percentage
    
# helper function : identify Tren rental bike 
def tren_rental_bike(df):
    yearly_rentals = df.groupby(by=["mnth_x", "tahun_x"]).agg({
        "cnt_x": "mean",
        "cnt_y": "sum"
    }).reset_index()

    yearly_rentals.rename(columns={
        "mnth_x" : "bulan",
        "tahun_x" : "tahun",
    }, inplace=True)

    return yearly_rentals

# define data
# bike_data = pd.read_csv('https://raw.githubusercontent.com/RizkiRdm/bike-sharing-analytict/refs/heads/main/dashboard/bike_data.csv', parse_dates=["dteday"])
bike_data = pd.read_csv('dashboard/bike_data.csv', parse_dates=["dteday"])

# call function
# filtered_data = filter_weather_sum_bike(bike_data)
tren_rental_bike_data = tren_rental_bike(bike_data)

# color palette
colors = ["#69b3a2", "#4374B3"]

# START MAKE A DASHBOARD
st.title("Data Analisis Bike Sharing")

# SECTION 1
col1, col2 = st.columns(2)

with col1:
    st.image("dashboard/logo.jpg")
with col2:
    st.text("Name : Rizki Romdhoni")
    st.text("Dataset : Bike Sharing Dataset")
    st.text("Hobby : Sleep")
    st.text("ID Dicoding : rizki_romdhoni_rvM9")
    st.text("Email : rizkimvp27@gmail.com")
    
st.divider()

# SECTION 2 

st.header("Bagaimana cuaca memengaruhi jumlah penyewaan sepeda ?")

# Buat dropdown untuk memilih musim dan cuaca
musim_options = bike_data['musim'].unique()
musim_selected = st.selectbox('Pilih Musim', musim_options)
# Filter data berdasarkan pilihan
filtered_data = bike_data[bike_data['musim'] == musim_selected]

# Pastikan tipe data sudah benar
filtered_data['cuaca'] = filtered_data['cuaca'].astype('category')
filtered_data['cnt_x'] = pd.to_numeric(filtered_data['cnt_x'])

cuaca_sum = filtered_data.groupby(by=['cuaca', 'tahun_x'])['cnt_x'].sum().reset_index()


st.divider()

fig = px.bar(cuaca_sum, 
              x='cuaca', 
              y='cnt_x',
              color="tahun_x" if 'tahun_x' in cuaca_sum.columns else None,
              labels={'cuaca': 'Kondisi Cuaca', 'cnt_x': 'Jumlah Penyewaan Harian', 'tahun_x' : "Tahun"},
              title=f'Jumlah Penyewaan Sepeda per Cuaca pada Musim {musim_selected}')
fig.update_layout(xaxis_tickangle=-45)
fig.update_yaxes(tickformat=',.0f')
st.plotly_chart(fig)

# expander
with st.expander("Insights"):

    st.write("- Cuaca Cerah: Merupakan kondisi cuaca yang paling disukai untuk bersepeda, menghasilkan jumlah penyewaan tertinggi.\n - Musim Panas: Merupakan musim dengan jumlah penyewaan sepeda tertinggi secara keseluruhan.\n - Cuaca Hujan: Mempengaruhi penurunan jumlah penyewaan sepeda secara signifikan.\n- Fluktuasi Musiman: Jumlah penyewaan sepeda bervariasi antar musim, dengan musim panas sebagai puncaknya dan musim dingin sebagai titik terendahnya.\n- Kondisi Berawan: Memberikan jumlah penyewaan yang moderat, tidak terlalu tinggi atau rendah.")

st.divider()

# section 3

st.header("Bisakah kita mengidentifikasi jam-jam puncak penyewaan sepeda setiap hari ?")

min_date = bike_data['dteday'].min().date()
max_date = bike_data['dteday'].max().date()

# unique_dates = bike_data['dteday'].dt.date.astype('str').unique()
day_selected = st.date_input(
    'Pilih Hari Penyewaan sepeda',
    value=(min_date, max_date),
    min_value=min_date,
    )

# Filter data
# df_filtered = bike_data[bike_data['dteday'].dt.date.astype('str') == str(day_selected)]

if len(day_selected) == 2:
    start_date, end_date = day_selected
    df_filtered = bike_data[(bike_data['dteday'].dt.date >= start_date) & 
                            (bike_data['dteday'].dt.date <= end_date)]


    # cek apakah tanggal penyewaan ada
    if not df_filtered.empty:
        total_rentals = df_filtered['cnt_y'].sum()   
        fig = px.bar(df_filtered,
                     x='hr', 
                     y='cnt_y', 
                     color='musim', 
                    hover_data=['hr'],
                    title=f'Total penyewaan sepeda harian berdasarkan Jam ({start_date} - {end_date})'
        )

        fig.update_layout(
            xaxis_title='Jam',
            yaxis_title='Jumlah Penyewaan',
            hovermode='x unified',
            template='plotly_dark', 
            title_font=dict(size=20)
        )
        
        fig.update_traces(hovertemplate="<br>".join([
            "Jumlah Penyewaan: %{y}",
            "Jam: %{x}"
        ]))
        
        st.plotly_chart(fig)

        # tampilkan total penyewaan sepeda dalam rentang waktu
        st.write(f"##### Total Penyewaan Sepeda: {total_rentals:,} sepeda")
    else:
        st.warning("Tidak ada data untuk rentang tanggal yang dipilih.")
else:
    st.warning("Pilih rentang tanggal lengkap")

# expander
with st.expander("Insights"):

    st.write("- Dari plot tersebut bisa disimpulkan jika jumlah terbanyak orang dalam menyewa sepeda ada di jam delapan pagi sampai ke jam lima sore.\n- Baik di tahun 2011 dan tahun 2012, jam lima sore memiliki jumlah penyewaan terbesar.")
    
st.divider()

# section 4
st.header("Berapa persen peningkatan penyewaan sepeda pada akhir pekan dibandingkan hari kerja ?")

# Hitung persentase
holiday_percentage, workingday_percentage = percent_rent_bike(bike_data)

bike_data['day_of_week'] = bike_data['dteday'].dt.day_name()
weekly_trend = bike_data.groupby('day_of_week')['cnt_x'].mean().reset_index()

day_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
weekly_trend['day_of_week'] = pd.Categorical(weekly_trend['day_of_week'], categories=day_order, ordered=True)

weekly_trend = weekly_trend.sort_values('day_of_week')

labels = ['Hari Kerja', 'Akhir Pekan']
percentages = [holiday_percentage, workingday_percentage]

# buat dataframe baru
chart_data = pd.DataFrame({
    'Labels' : labels,
    'Percentage' : percentages
})



# Bar Chart
fig_bar_chart = px.bar(
    chart_data,
    x="Labels",
    y="Percentage",
    color="Labels",
    text="Percentage",
    title="Distribusi Penyewaan Sepeda",
    color_discrete_sequence=["#636EFA", "#EF553B"],
    text_auto=".1f %"
)

fig_bar_chart.update_layout(
    xaxis_title="Jenis Hari",
    yaxis_title="Persentase Penyewaan (%)",
    template="plotly_white"
)

# line chart
fig_line_chart = px.line(
    weekly_trend,
    x="day_of_week",
    y="cnt_x",
    title="Tren penyewaan sepeda dalam seminggu",
    markers=True,
    labels={
        "day_of_week": "Hari", 
        "cnt_x": "Rata-rata Penyewaan"
    }
)

fig_line_chart.update_layout(template="plotly_white")

# tampilkan chart
st.plotly_chart(fig_bar_chart, use_container_width=True)
st.plotly_chart(fig_line_chart, use_container_width=True)


with st.expander("Insight"):
    st.text("Penyewaan pada akhir pekan menunjukan penurun yang cukup besar, bisa disimpulkan penyebabnya adalah karena orang pada akhir pekan lebih sedikit melakukan aktivitas, seperti berangkat kerja. Berbandingkan terbalik jika di hari kerja, orang lebih banyak melakukan aktivitas seperti berangkat kerja, pergi ke sekolah atau aktivitas lainyya.")
    
st.divider()

# SECTION 5
st.header("Bagaimana tren penyewaan sepeda berubah dari tahun 2011 ke 2012 ?")
col1, col2 = st.columns(2, gap="small")

with col1:
    fig, ax = plt.subplots(figsize=(14, 9))

    sns.lineplot(
    x="bulan",
    y="cnt_y",
    hue="tahun",
    data=tren_rental_bike_data,
    ax=ax,
    palette=colors
    )

    # Customizing the chart
    ax.set_title("Jumlah total Penyewaan Sepeda Berdasarkan Bulan dan Tahun", fontsize=22)
    ax.set_xlabel("Bulan", fontsize=16)
    ax.set_ylabel("Jumlah Penyewaan", fontsize=16)
    plt.xticks(range(1,13))
    plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))

    # Render chart in Streamlit
    st.pyplot(fig)
    
with col2:
    fig, ax = plt.subplots(figsize=(14, 9))

    sns.barplot(
    x="bulan",
    y="cnt_x",
    hue="tahun",
    data=tren_rental_bike_data,
    ax=ax,
    palette=colors
    )

    # Customizing the chart
    ax.set_title("Jumlah Penyewaan Sepeda Harian Berdasarkan Bulan dan Tahun", fontsize=22)
    ax.set_xlabel("Bulan", fontsize=16)
    ax.set_ylabel("Jumlah Penyewaan", fontsize=16)
    plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))

    # Render chart in Streamlit
    st.pyplot(fig)

with st.expander("insight"):
    st.write("- Jumlah penyewaan sepeda dari tahun 2011 sampai tahun 2012 mengalami peningkatan yang cukup besar.\n- Rata-rata jumlah penyewaan sepeda di tahun 2012 ada di angka 3.000 sampai diatas 7.000 sepeda dan terbanyak ada di bulan september (9) di tahun 2012.\n- Terdapat pola musiman yang jelas pada jumlah penyewaan sepeda. Jumlah penyewaan cenderung meningkat pada bulan-bulan tertentu seperti dari bulan maret (3) sampai bulan september (9) dan menurun pada bulan-bulan seperti bulan oktober (10) sampai bulan februari (2). Ini menunjukkan bahwa faktor cuaca, musim, atau event tertentu dapat mempengaruhi minat masyarakat untuk menyewa sepeda.")