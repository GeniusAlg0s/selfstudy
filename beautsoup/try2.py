import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
import time
import altair as alt
from vega_datasets import data
import pandas as pd

st.title('animation')

cars = data.cars()
print("NEWWWWWW RUUUUNNNNN -------------------------- NEEEWWWWW RUUUNNN")
# print(cars)
# #try to split the cars into 3 listg based on a key

##  CHADS HINT   newdf= origdf["sorted"] -Chad help sort the df first  by origin and then make a new df based off of that

ucars = cars.loc[cars['Origin'] == 'USA'] 
jcars = cars.loc[cars['Origin'] == 'Japan']
ecars = cars.loc[cars['Origin'] == 'Europe']

# print("NEWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW")
# print('USA CARS--------USA CARS--------USA CARS----------')
# print(ucars)
# print('JAPAN CARS--------JAPAN CARS--------JAPAN CARS----------')
# print(jcars)
# print('EUROPE CARS--------EUROPE CARS--------EUROPE CARS----------')
# print(ecars)

df = cars['Horsepower']
ew = cars['Acceleration']

dfu = ucars['Horsepower']
dfe = ecars['Horsepower']
dfj = jcars['Horsepower']
dfj2 = jcars['Weight_in_lbs']

blank_chart = alt.Chart(cars).mark_line().encode()

basic_chart = alt.Chart(cars).mark_line().encode(
    x='Horsepower',
    y='Weight_in_lbs',
    color='Origin',
    # legend=alt.Legend(title='Animals by year')
)
basic_chart1 = alt.Chart(ucars).mark_line().encode(
    x='Horsepower',
    y='Weight_in_lbs',
    color='Origin',
    # legend=alt.Legend(title='Animals by year')
)
basic_chart2 = alt.Chart(jcars).mark_line().encode(
    x='Horsepower',
    y='Weight_in_lbs',
    color='Origin',
    # legend=alt.Legend(title='Animals by year')
)

progress_bar = st.progress(0)
status_text = st.empty()
# chart = st.altair_chart(basic_chart1)
chart = st.line_chart(df)

# chart = st.line_chart(np.random.randn(10, 2))

for i in range(len(cars)-1):
    # Update progress bar.
    progress_bar.progress(i + 1)

    #print(cars)
    for i in cars:
        # print(i)
        
        # new_rows= dfj
        new_rows = {}
        new_rows = i['Acceleration']
    # new_rows = np.random.randn(10, 2)

    # Update status text.
    status_text.text(
        'adding acceleration data: ')

    # status_text.text(
    #     'The latest random number is: %s' % new_rows[-1, 1])

    # Append data to the chart.
    chart.add_rows(new_rows)

    # Pretend we're doing some computation that takes time.
    time.sleep(0.1)

status_text.text('Done!')
st.balloons()

