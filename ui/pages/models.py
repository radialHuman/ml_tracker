'''
DOCUMENTATION
=============

First page to show
1. Various modesl and there performace
'''

import streamlit as st
from utils.util import General as fun
from pandas import DataFrame


def app():
    model_df = DataFrame(fun.read_model_data())
    model_metric = model_df["result"][0].keys()
    parameter_metric = model_df["parameters"][0].keys()
    metric_dict = {}
    for m in model_metric:
        metric_dict[m] = []
    for i in model_df.index:
        for m in model_metric:
            metric_dict[m].append(model_df["result"][i][m])

    parameter_dict = {}
    for m in parameter_metric:
        parameter_dict[m] = []
    for i in model_df.index:
        for m in parameter_metric:
            parameter_dict[m].append(model_df["parameters"][i][m])

    metric_df = DataFrame(metric_dict)
    parameter_df = DataFrame(parameter_dict)
    metric_df.index = model_df["model_name"]
    parameter_df.index = model_df["model_name"]
    details_df = metric_df.join(parameter_df)
    st.table(details_df)

    for col in metric_df.columns:
        st.header(f'{col} : ')
        st.bar_chart(metric_df[col])
