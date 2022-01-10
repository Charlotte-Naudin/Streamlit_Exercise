import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_icon="🚗", layout="wide")

st.title('🚗 **CARS - DATA ANALYSIS**')

link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
df_cars = pd.read_csv(link)
df_cars_Europe = df_cars[(df_cars["continent"] == 'Europe.') | (df_cars["continent"] == ' Europe.')]
df_cars_US = df_cars[df_cars["continent"] == ' US.']
df_cars_Japan = df_cars[df_cars["continent"] == ' Japan.']

option = st.selectbox('Select an area', ('all areas', 'Europe', 'US', 'Japan'))
st.write('You have selected : ', option)

col1, col2, col3 = st.columns(3)

with col1:
    st.header('**Dataframe**')
    st.text('First 10 rows')
    if option == 'all areas':
        st.dataframe(data=df_cars)
    elif option == 'Europe':
        st.dataframe(df_cars_Europe)
    elif option == 'US':
        st.dataframe(df_cars_US)
    else:
        st.dataframe(df_cars_Japan)

with col2:
    st.header("**Correlation**")
    if option == 'all areas':
        fig = plt.figure(figsize=(12, 5))
        sns.heatmap(df_cars.corr(), center=0, cmap=sns.color_palette('vlag', as_cmap=True))
        st.pyplot(fig)
        st.text("We can see that there are strong positive correlations between : \n - cylinders and cubicinches\n - weightlbs and cubicinches \n\nThere are also strong negative correlations between : \n - mpg and weightlbs \n - hp and time-to-60")
    elif option == 'Europe':
        fig = plt.figure(figsize=(12, 5))
        sns.heatmap(df_cars_Europe.corr(), center=0, cmap=sns.color_palette('vlag', as_cmap=True))
        st.pyplot(fig)
        st.text("We can see that there is a strong positive correlation between : \n - weightlbs and cubicinches \n\nThere are also strong negative correlations between : \n - hp and mpg \n - hp and time-to-60")
    elif option == 'US':
        fig = plt.figure(figsize=(12, 5))
        sns.heatmap(df_cars_US.corr(), center=0, cmap=sns.color_palette('vlag', as_cmap=True))
        st.pyplot(fig)
        st.text("We can see that there are strong positive correlations between : \n - cubicinches and cylinders / hp / weightlbs\n\nThere are also strong negative correlations between : \n - mpg and weightlbs / cubicinches / cylinders \n - hp and time-to-60")
    else:
        fig = plt.figure(figsize=(12, 5))
        sns.heatmap(df_cars_Japan.corr(), center=0, cmap=sns.color_palette('vlag', as_cmap=True))
        st.pyplot(fig)
        st.text("We can see that there are positive correlations between : \n - cubicinches and weightlbs\n - weightlbs and hp \n\nThere are also negative correlations between : \n - mpg and hp \n - hp and time-to-60")

with col3:
    st.header("**Distribution**")
    if option == 'all areas':
        fig = plt.figure(figsize=(12, 5))
        plot2 = sns.histplot(data=df_cars, x=df_cars['weightlbs'], bins=10, kde=True, color='mediumaquamarine')
        st.pyplot(fig)
        st.text("Most cars in all areas considered have a weightlbs between 2000 and 3000.")
    elif option == 'Europe':
        fig = plt.figure(figsize=(12, 5))
        plot2 = sns.histplot(data=df_cars_Europe, x=df_cars_Europe['weightlbs'], bins=10, kde=True, color='mediumaquamarine')
        st.pyplot(fig)
        st.text("Most cars in Europe have a weightlbs between 1800 and 2200.")
    elif option == 'US':
        fig = plt.figure(figsize=(12, 5))
        plot2 = sns.histplot(data=df_cars_US, x=df_cars_US['weightlbs'], bins=10, kde=True, color='mediumaquamarine')
        st.pyplot(fig)
        st.text("The range of weightlbs for cars in the US is large,. \nIt goes from 2400 to 4700. \nCars are heavier than in other areas. ")
    else:
        fig = plt.figure(figsize=(12, 5))
        plot2 = sns.histplot(data=df_cars_Japan, x=df_cars_Japan['weightlbs'], bins=10, kde=True, color='mediumaquamarine')
        st.pyplot(fig)
        st.text("Most cars in Japan have a weightlbs around 2000-2100.")
