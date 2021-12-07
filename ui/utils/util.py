'''
DOCUMENTATION
=============

Functions page with
1. variables used
2. classes based on pages and corresponding functions

'''
from pandas import read_csv, DataFrame, merge, date_range, read_excel, Series
from datetime import datetime, timedelta
from numpy import nan
import streamlit as st
from json import load
# from glob import glob
# from os.path import getctime
from supabase_py import create_client, Client


today = int(str(datetime.now()).split(" ")[0].replace("-", ""))
cred = load(open('../configuration/sbConfig.json'))
supabase: Client = create_client(cred["db"], cred["key"])


class General:
    def read_model_data():
        return supabase.table("tracker").select("*").execute()["data"]

    def read_cleaned_data(data_set):
        return read_csv(data_set)

    def show_data_text():
        return "Something Data"
