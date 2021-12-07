'''
DOCUMENTATION
=============

Third page to
1. Use seletced model from
2. User single input based on features
3. User upload csv based on features to generate table 
'''

import streamlit as st
from utils.util import General as fun
from pandas import DataFrame
from pickle import load
from glob import glob
from numpy import array


def app():
    st.header("Generate output based on model selection")
    # model slection
    df = DataFrame(fun.read_model_data())
    model_list = ["None"]+list(df["model_name"])
    model_selection = st.selectbox(
        "Which model needs to be tested?", model_list)
    if(model_selection != "None"):
        selected_model = load(open(f'../model/{model_selection}', 'rb'))
        st.text(selected_model)

    # data selection
    cleaned_data_list = ["None"]+glob("..\\data\\cleaned\\*.csv")
    data_selection = st.selectbox(
        "Which data is it based on", cleaned_data_list)
    if(data_selection != "None"):
        selected_df = fun.read_cleaned_data(data_selection)
        st.dataframe(selected_df.describe())

    # user input
    # TODO read that model from storage when its ready, untill then use it from model folder of the project
    if(model_selection != "None"):
        target = df[df["model_name"] == model_selection]["target"].values[0]
        single_, csv_upload_ = st.columns([1, 1])
        with single_:
            show_features_with_user_input(
                df[df["model_name"] == model_selection]["features"].values[0], target, selected_model)
        with csv_upload_:
            show_upload_options(selected_model)


def show_features_with_user_input(features, target, selected_model):
    single_output = "NA"
    # TODO show features 1/1 and text box to enter with hint/range
    user_input = {i: 0.0 for i in features}  # initial 0
    st.header("Enter values as float")
    for i in features:
        user_input[i] = st.text_input(i, user_input[i])
    if st.button("Generate Output"):
        single_output = generate_single_output(user_input, selected_model)[0]
        st.header(f"{target} for the entered values is  :  {single_output}")


def generate_single_output(user_input, selected_model):
    # convert all to float and procceed
    if("" not in user_input.values()):
        user_input = {i: float(j) for i, j in user_input.items()}
    return selected_model.predict(array(list(user_input.values())).reshape(1, 11))


def show_upload_options(selected_model):
    # TODO ask to upload csv and scorll down to submit and show output
    if st.button("Generate output"):
        # TODO generate using the model sleected
        ""
    return
