import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
import time
import altair as alt
from vega_datasets import data
import pandas as pd
from PIL import Image

st.title('SELF STUDY')

st.title('animation')
img= Image.open('bald_eagle.png')

st.image(img,width=200 )

st.markdown("here is a away to get the equivalent of a an html <p>elemnt</p> here we \n are taking data from a json file and displaying the contents in an animated fashion \n still working on making it pretty at the end you should see some baloons")
cars = data.cars()
# print(cars)
# #try to split the cars into 3 listg based on a key

##     newdf= origdf["sorted"] -Chad help sort the df first  by origin and then make a new df based off of that

ucars = cars.loc[cars['Origin'] == 'USA'] 
jcars = cars.loc[cars['Origin'] == 'Japan']
ecars = cars.loc[cars['Origin'] == 'Europe']

#make new list and try to feed the values into chart
carlist = []
print("*********************************************************************")
for i in ucars['Displacement']:
    carlist.append(i)


df2 = carlist
#GOOOODDDD COOOODDEEE
df = ucars['Miles_per_Gallon']
# df2 = cars['Horsepower']
#GOOOODDDD COOOODDEEE ^^^^^^^^^^^^^^^^^^^^^^^^



progress_bar = st.progress(50)
status_text = st.empty()
chart = st.line_chart(df)


for i in range(100):
    # Update progress bar.
    progress_bar.progress(i + 1)

    #print(cars)
    # for i in jcars:
    for i in cars:
        # print(jcars['Miles_per_Gallon'])
        
        new_rows= df2
        # new_rows = {}
        # new_rows[i] = i['Acceleration']
   

    # Update status text.
    status_text.text(
        'adding  data to chart yeah it takes awhile: ')

   

    # Append data to the chart.
    chart.add_rows(new_rows)

    # Pretend we're doing some computation that takes time.
    time.sleep(0.01)

status_text.text('Done!')
st.balloons()