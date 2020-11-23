import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
from datetime import date
from datetime import datetime

def to_int(x):

    if pd.isna(x):
        return x

    elif x.find('(')==-1:
        return int(x.replace('.', ''))

    return int(x[:x.find('(')].replace('.', ''))

@st.cache(suppress_st_warning=True)
def load_data(fname):
    data_load_state = st.text('Carregando dados...')
    df = pd.read_csv(fname, sep=';')
    df.loc[df['regiao'].eq('Brasil'), 'estado'] = 'BR'
    df['populacaoTCU2019'] = df['populacaoTCU2019'].astype('Int64')
    df['data'] = df['data'].pipe(pd.to_datetime, errors='coerce')
    data_load_state.text("")
    return df

def get_min_date(data):
    return data['data'].dt.date.min()

def get_states(data):
    return list(data['estado'].dropna().unique())

def show_graph_by_states(df, estados, rolling, per_millon, cum_sum, brazil, starting_date):

    starting_date = datetime.combine(starting_date, datetime.min.time())

    if brazil:
        estados += ['BR']

    df_tmp = df.loc[df['estado'].isin(estados)&df['municipio'].isna()&df['data'].ge(starting_date), ['estado', 'data', 'obitosNovos', 'populacaoTCU2019']].copy()

    df_tmp = df_tmp.sort_values('data').dropna()

    df_tmp['obitosNovos'] = df_tmp.groupby('estado')['obitosNovos'].transform(lambda x: x.rolling(rolling).mean())

    if per_millon:
        df_tmp['obitosNovos'] = 1000000*df_tmp['obitosNovos']/df_tmp['populacaoTCU2019']

    if cum_sum:
        df_tmp['obitosNovos'] = df_tmp.groupby('estado')['obitosNovos'].transform(lambda x: x.cumsum())


    chart = alt.Chart(df_tmp).mark_line(point=True).encode(x='data', y='obitosNovos', color='estado').properties(width=950, height=600)
    st.altair_chart(chart)
