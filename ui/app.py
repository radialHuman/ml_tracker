'''
DOCUMENTATION
=============

Main page with
1. Multi-page app routing
2. Layout and other configurations

'''


from utils.multi_page import MultiApp
from pages import models, data, use_model, insights
import streamlit as st
# from PIL import Image


# setting up page layout
st.set_page_config(layout="wide",
                   #    page_icon=Image.open(""),
                   page_title="MODEL PERFORMANCE")
# hidding extra stuff from page
hide_extra = '''
<style>
#MainMenu {visibility : hidden;}
footer {visibility : hidden;}
</style>
'''
st.markdown(hide_extra, unsafe_allow_html=True)

# logo
# st.image(Image.open(""), width=100)

# build multi page navgation
app = MultiApp()
app.add_app("Models", models.app)
app.add_app("Data", data.app)
app.add_app("Run model", use_model.app)
app.add_app("Insights", insights.app)
app.run()
