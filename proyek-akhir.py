import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

st.title('Bike Sharing Dataset :sparkles:')

day_df = pd.read_csv("https://raw.githubusercontent.com/Farisyy/Proyek-Analisis-Data/main/data/day.csv")
hour_df = pd.read_csv("https://raw.githubusercontent.com/Farisyy/Proyek-Analisis-Data/main/data/hour.csv")

st.header('Average Rent by Season, Day, and Hour')

tab1, tab2, tab3 = st.tabs(["Season", "Day", "Hour"])
 
with tab1:
    st.subheader('Average Rent by Season')

    flavors = ('Spring', 'Summer', 'Fall', 'Winter')
    votes = (day_df.groupby(by="season").cnt.mean())
    colors = ('#93C572', '#E67F0D', '#8B4513', '#FFF8DC')
    explode = (0, 0, 0.1, 0)
    
    fig, ax = plt.subplots()
    ax.pie(x=votes, labels=flavors, colors=colors, explode=explode, wedgeprops = {'width': 0.4})
    st.pyplot(fig)

    st.caption('Donut plot Average Rent by Season')

    with st.expander("See explanation"):
        st.write(
            """
            Dari hasil donut plot di atas, dapat dilihat bahwa penyewaan terbanyak dilakukan pada musim gugur.
            """
        )
 
with tab2:
    st.subheader('Average Rent by Day')

    byweekday_df = day_df.groupby(by="weekday").cnt.mean().sort_values(ascending=False)

    colors = ["#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]
    
    fig, ax = plt.subplots()
    byweekday_df.plot(kind="bar", color=colors, ax=ax)
    plt.title("Average Rental by Day", loc="center", fontsize=15)
    plt.ylabel("Average")
    plt.xlabel("Day")
    plt.xticks(rotation=0)
    st.pyplot(fig)

    st.caption('Bar chart Average Rent by Day')

    with st.expander("See explanation"):
        st.write(
            """
            Dari hasil visualisasi yang didapatkan, terlihat bahwa pelanggan melakukan penyewaan terbanyak pada hari ke-5 atau hari jumat.
            """
        )
 
with tab3:
    st.subheader('Average Rent by Hour')

    byhour_df = hour_df.groupby(by="hr").cnt.mean().sort_values(ascending=False)

    colors = ["#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]

    fig, ax = plt.subplots()
    byhour_df.plot(kind="bar", color=colors, ax=ax)
    plt.title("Average Rental by Hour", loc="center", fontsize=15)
    plt.ylabel("Average")
    plt.xlabel("Hour")
    plt.xticks(rotation=0)
    st.pyplot(fig)
    
    st.caption('Bar chart Average Rent by Hour')

    with st.expander("See explanation"):
        st.write(
            """
            Dari hasil bar chart di atas, dapat dilihat bahwa pelanggan paling banyak melakukan penyewaan pada jam 17:00 atau jam 5 sore.
            """
        )
 
with st.container():
    st.header('Correlation between Humidity and Total Rent')

    humidity = day_df["hum"]
    rent = day_df["cnt"]
    
    fig, ax = plt.subplots()
    sns.scatterplot(x=humidity, y=rent, ax=ax)
    sns.regplot(x=humidity, y=rent, ax=ax)
    plt.title("Correlation between Humidity and Total Rent", loc="center", fontsize=15)
    plt.ylabel("Total rent")
    plt.xlabel("Humidity")
    st.pyplot(fig)

    st.caption('Bar chart Average Rent by Hour')

    with st.expander("See explanation"):
        st.write(
            """
            Dapat dilihat dari scatter plot di atas, kelembapan mempengaruhi jumlah penyewaan. Semakin lembab udara disekitar, semakin meningkat jumlah penyewaan.
            """
        )
 
with st.container():
    st.header('Comparison between Rent in Holiday/Weekend and Workday')

    kind = ('Weekend or Holiday', 'Workingday')
    rents = (day_df.groupby(by="workingday").cnt.mean())
    colors = ('#93C572', '#E67F0D')
    explode = (0, 0)
    
    fig, ax = plt.subplots()
    ax.pie(x=rents, labels=kind, autopct='%1.1f%%', colors=colors, explode=explode,)
    st.pyplot(fig)

    st.caption('Pie chart Comparison between Rent in Holiday/Weekend and Workday')

    with st.expander("See explanation"):
        st.write(
            """
            Dari hasil pie chart yang dilakukan, terlihat bahwa rata-rata penyewaan pada hari kerja lebih banyak dibandingkan dengan hari libur atau weekend.
            """
        )