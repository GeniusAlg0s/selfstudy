# app.py, run with 'streamlit run app.py'
import pandas as pd
import streamlit as st
import altair as alt
import csv
import numpy as np
from vega_datasets import data
from urllib.error import URLError

#with open('xmen.csv', newline='') as csvfile:
    #spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    #for row in spamreader:
         #print(', '.join(row))


st.title('Car data by the biggest car producers')

cars = data.cars()

ca= alt.Chart(cars).mark_point().encode(
    x='Cylinders',
    y='Acceleration',
    color='Origin',
   # shape='Origin'
)
md= alt.Chart(cars).mark_point().encode(
    x='Miles_per_Gallon',
    y='Displacement',
    color='Origin',
   # shape='Origin'
)
wa= alt.Chart(cars).mark_point().encode(
    x='Weight_in_lbs',
    y='Acceleration',
    color='Origin',
   # shape='Origin'
)
bbr= alt.hconcat(
   ca,
   md,
   wa
)
# bbr= alt.hconcat(
#    ca.encode(color='Cylinders:Q').properties(title='quantitative'),
#    md.encode(color='Cylinders:O').properties(title='ordinal'),
#    wa.encode(color='Cylinders:N').properties(title='nominal'),
# )
# alt.vconcat(
#    base.encode(color='Cylinders:Q').properties(title='quantitative'),
#    base.encode(color='Cylinders:O').properties(title='ordinal'),
#    base.encode(color='Cylinders:N').properties(title='nominal'),
# )
st.write(bbr)
st.balloons()