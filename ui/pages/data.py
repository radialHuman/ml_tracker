'''
DOCUMENTATION
=============

Second page to show (TODO)
1. To show version fo data stored
'''

import streamlit as st
from utils.util import General as fun


def app():
    st.text(fun.show_data_text())
