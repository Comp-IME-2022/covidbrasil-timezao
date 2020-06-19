import os

import datetime
import streamlit as st
import yaml

import utils

with open("params.yaml", "r") as f:
    params = yaml.load(f, yaml.Loader)

st.title("Progressão Temporal COVID-19 Brasil")

data = utils.load_data(os.path.join(params['data_dir'], params['fname']))

rolling = st.sidebar.number_input("Rolling", min_value=1, step=1, max_value=14)
estados = st.sidebar.multiselect("Estados", options=utils.get_states(data))
per_millon = st.sidebar.checkbox("Por milhão")
starting_date = st.sidebar.date_input("A partir da data:", min_value=utils.get_min_date(data), value=utils.get_min_date(data))
cum_sum = st.sidebar.checkbox("Acumulado")
brazil = st.sidebar.checkbox("Nacional")

utils.show_graph_by_states(data, estados=estados, rolling=rolling, per_millon=per_millon, cum_sum=cum_sum, brazil=brazil, starting_date=starting_date)
