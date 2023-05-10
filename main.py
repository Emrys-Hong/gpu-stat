import streamlit as st
import pandas as pd

st.title("DeCLaRe GPU monitoring system")

chart_option = st.selectbox(
    "Select Machine: ",
    ('Total',
     '172.17.240.73',
     '172.18.240.107',
     '172.18.240.119',
     '172.17.240.253',
     '172.18.240.231',
     '172.18.240.195',
     '172.18.240.100',
     )
)

def create_line_chart(ip):
    if ip == "total":
        df = pd.concat([
            pd.read_csv(
             '172.17.240.73',
             '172.18.240.107',
             '172.18.240.119',
             '172.17.240.253',
             '172.18.240.231',
             '172.18.240.195',
             '172.18.240.100',
            )
        ])
    else:
        df = pd.read_csv(ip + '_gpu_log.csv')

    grouped_df = df.groupby(['date', 'user']).size().reset_index(name='count')

    pivot_df = grouped_df.pivot_table(index='date', columns='user', values='count', fill_value=0)

    breakpoint()
    pivot_table = pd.pivot_table(
        df, 
        values='user', 
        index=['date'], columns=['user'],
        aggfunc=pd.Series.count
    )
    return pivot_table


st.line_chart(
    create_line_chart(chart_option)
)



