import streamlit as st
import pandas as pd
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv (r'irondata.csv')
st.write(df)
bike_df = df.loc[df['Sport'] == "Bike"]
bike_df.drop(['Kadenz', 'Beckenlänge', 'Bahnen', 'Züge-100m'], axis = 1, inplace = True)
bike_df.fillna(bike_df.mean(), inplace=True)
st.write(bike_df)

data = {'Average Watts': bike_df["Average Watts"],
        'Pace': bike_df["Pace"],
        'HR': bike_df["Heart Rate Average"]}

bike_average_watts = pd.DataFrame(data['Average Watts'])
bike_pace = pd.DataFrame(data["Pace"])
bike_HR = pd.DataFrame(data["HR"])

st.header("IronData")


st.markdown("### Run")

st.markdown("### Bike")
col1, col2, col3 = st.columns(3)
with col1:
    st.line_chart(bike_average_watts)
with col2:
    st.line_chart(bike_pace)
with col3:
    st.line_chart(bike_HR)
st.markdown("### Swim")
