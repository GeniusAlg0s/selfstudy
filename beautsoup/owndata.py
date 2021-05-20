
import pandas as pd
import streamlit as st
import altair as alt
import csv
import numpy as np
from vega_datasets import data
from urllib.error import URLError


       
st.title('SELF STUDY')


st.title('using streamlit data to enter into web form and return it on the page \n no need for shbang line as you can run with streamlit run <file>')

st.markdown("Streamlit connects the worlds of Python and React\n Each Streamlit call on the Python side loads up a React component from the running Streamlit server,\nwhich is then rendered onto your web browser")

st.markdown("below shows how streamlit can take input and render html elments based on that input")

name = st.text_input("Enter your name:")
age = st.slider("what month where you born in:", min_value=1, max_value=12)
stone = ""
if age == 1:
      stone = "Garnet"
elif age == 2:
      stone = "Amethyst"
elif age == 3:
      stone = "Aquamarine"
elif age == 4:
      stone = "Diamond"
elif age == 5:
      stone = "Emerald"
elif age == 6:
      stone = "Pearl"
elif age == 7:
      stone = "Ruby"
elif age == 8:
      stone = "Peridot"
elif age == 9:
      stone = "Sapphire"
elif age == 10:
      stone = "Opal"
elif age == 11:
      stone = "Topaz"
elif age == 12:
      stone = "Zircon"



st.write(f"Hi, ", name ,"you where born on the ", age, " month and you stone is: ", stone)

st.title('Legacy Car data by the biggest car producers Europe Japan USA')
cars = data.cars()

ca= alt.Chart(cars).mark_point().encode(
   x='Cylinders',
   y='Acceleration',
   color='Origin',
   shape='Origin'
)
md= alt.Chart(cars).mark_point().encode(
   x='Miles_per_Gallon',
   y='Displacement',
   color='Origin',
   shape='Origin'
)
wa= alt.Chart(cars).mark_point().encode(
   x='Weight_in_lbs',
   y='Acceleration',
   color='Origin',
   shape='Origin'
)
bbr= alt.vconcat(
   ca,
   md,
   wa
)

st.write(bbr)
st.balloons()
