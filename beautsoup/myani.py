
import streamlit as st
import time
from vega_datasets import data
from PIL import Image

st.title('SELF STUDY')

agree = st.checkbox('want to see my work')
if agree:
    st.title('animation')
    img= Image.open('bald_eagle.png')

    st.image(img,width=200 )

    st.markdown("here is a away to get the equivalent of a an html <p>elemnt</p> here we \n are taking data from a json file and displaying the contents in an animated fashion \n still working on making it pretty at the end you should see some baloons")
    cars = data.cars()

    #split the dataframe did have time to full utilize all of the data that i created
    ucars = cars.loc[cars['Origin'] == 'USA'] 
    jcars = cars.loc[cars['Origin'] == 'Japan']
    ecars = cars.loc[cars['Origin'] == 'Europe']

    #make new list and try to feed the values into chart
    carlist = []
   
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

        for i in cars:
            new_rows= df2
        
        # Update status text.
        status_text.text(
            'adding  data to chart yeah it takes awhile: ')

        # Append data to the chart.
        chart.add_rows(new_rows)

        # Pretend we're doing some computation that takes time.
        time.sleep(0.01)

    status_text.text('Done!')
    st.balloons()