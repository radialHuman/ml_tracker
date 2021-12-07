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
    df = DataFrame(fun.read_model_data())
    model_groups = df["model_group"].unique()
    model_selected = st.selectbox("Which model group?",
                                  model_groups)
    model_df = df[df["model_group"] == model_selected]
    model_df.index = range(model_df.shape[0])
    model_metric = model_df["result"][0].keys()
    parameter_metric = model_df["parameters"][0].keys()

    # evaluation metrics
    metric_dict = {}
    for m in model_metric:
        metric_dict[m] = []
    for i in model_df.index:
        for m in model_metric:
            metric_dict[m].append(model_df["result"][i][m])

    # parameters used
    parameter_dict = {}
    for m in parameter_metric:
        parameter_dict[m] = []
    for i in model_df.index:
        for m in parameter_metric:
            parameter_dict[m].append(model_df["parameters"][i][m])

    # columns in the model
    feature_df = model_df[["model_name", "features"]]
    feature_df.index = feature_df["model_name"]
    feature_df = feature_df[["features"]]
    feature_df["features"] = feature_df["features"].apply(
        lambda x: (",\n").join(x))

    # combining them all
    metric_df = DataFrame(metric_dict)
    parameter_df = DataFrame(parameter_dict)
    metric_df.index = model_df["model_name"]
    parameter_df.index = model_df["model_name"]
    # details_df = metric_df.join(parameter_df)
    details_df = metric_df.join(parameter_df).join(feature_df)
    st.table(details_df)

    number_of_metrics = len(metric_df.columns)
    cols = st.columns([1]*number_of_metrics)
    for n, col in enumerate(metric_df.columns):
        with cols[n]:
            st.header(f'{col} : ')
            st.bar_chart(metric_df[col],  width=500, height=500,
                         use_container_width=False)
