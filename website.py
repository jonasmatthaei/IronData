import streamlit as st
import pandas as pd
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Raw Data
df = pd.read_csv (r'irondata.csv')

# Run
run_df = df.loc[df['Sport'] == "Run"]
run_df.drop(['Average Watts', 'Beckenlänge', 'Bahnen', 'Züge-100m'], axis = 1, inplace = True)
run_df.fillna(run_df.mean(), inplace=True)

run_data = {'Pace': run_df["Pace"],
            'Kadenz': run_df['Kadenz'],
            'HR': run_df['Heart Rate Average']}

run_pace = pd.DataFrame(run_data["Pace"])
run_kadenz = pd.DataFrame(run_data["Kadenz"])
run_HR = pd.DataFrame(run_data["HR"])

# Bike
bike_df = df.loc[df['Sport'] == "Bike"]
bike_df.drop(['Kadenz', 'Beckenlänge', 'Bahnen', 'Züge-100m'], axis = 1, inplace = True)
bike_df.fillna(bike_df.mean(), inplace=True)

bike_data = {'Average Watts': bike_df["Average Watts"],
        'Pace': bike_df["Pace"],
        'HR': bike_df["Heart Rate Average"]}

bike_average_watts = pd.DataFrame(bike_data['Average Watts'])
bike_pace = pd.DataFrame(bike_data["Pace"])
bike_HR = pd.DataFrame(bike_data["HR"])

# Swim
swim_df = df.loc[df['Sport'] == "Swim"]
swim_df.drop(['Elevation', 'Average Watts', 'Kadenz'], axis = 1, inplace = True)
swim_df.fillna(swim_df.mean(), inplace=True)

swim_data = {'Pace': swim_df["Pace"],
        'Züge': swim_df["Züge-100m"],
        'HR': swim_df["Heart Rate Average"]}

swim_pace = pd.DataFrame(swim_data['Pace'])
swim_zuege = pd.DataFrame(swim_data["Züge"])
swim_HR= pd.DataFrame(swim_data["HR"])


# Header
st.header("IronData 🦿")

# Run Section
st.markdown("### Run 🏃🏽")

st.line_chart(run_pace)

col2_run, col3_run = st.columns(2)
with col2_run:
    st.line_chart(run_kadenz)
with col3_run:
    st.line_chart(run_HR)


# Bike Section
st.markdown("### Bike 🚴🏽")
st.line_chart(bike_average_watts)

col2_bike, col3_bike = st.columns(2)
with col2_bike:
    st.line_chart(bike_pace)
with col3_bike:
    st.line_chart(bike_HR)


# Swim Section
st.markdown("### Swim 🏊🏽‍♂️")
st.line_chart(swim_pace)

col2_bike, col3_bike = st.columns(2)
with col2_bike:
    st.line_chart(swim_zuege)
with col3_bike:
    st.line_chart(swim_HR)
