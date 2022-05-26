import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
def run_eda() :
    df1 = pd.read_csv('data/dataset.csv')
    st.dataframe(df1)
    
    fig = px.pie(df1, names='Disease')
    st.plotly_chart(fig)
