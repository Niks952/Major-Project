import os
import streamlit as st
import numpy as np
from PIL import  Image

from multiple import MultiPage
from pages import base,recomend_poster

app = MultiPage()

# image = Image.open('dsu.jpg')
# st.image(image,width=125, use_column_width='never')
col1, col2 = st.columns(2)
# col1.image(display, width = 400)
# col2.title("Recommendation Engine")



app.add_page("Upload Data", base)
app.add_page("Change Metadata", recomend_poster)


# app.run()
