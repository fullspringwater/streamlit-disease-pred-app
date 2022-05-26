import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objs as go
import plotly.offline as pyo

def run_eda() :
    
    df1 = pd.read_csv('data/dataset.csv')

    # Disease Pie Chart
    fig1 = px.pie(df1, names='Disease',
                title = '질병 종류')
    st.plotly_chart(fig1)


    # 데이터의 NaN 값
    fig2 = px.imshow(df1.isnull(), 
                        color_continuous_scale='agsunset', 
                        title = 'NaN Data')
    st.plotly_chart(fig2)

    # 질병별 증상
    disease_list = df1['Disease'].unique().tolist()
    st.write()
    st.subheader('질병별 증상들 집계')
    choice = st.selectbox('질병 선택', disease_list)
    if st.button('결과') :
        if len(choice) != 0 :
            d1 = df1.loc[df1['Disease'] == choice,'Symptom_1'].value_counts().to_frame().reset_index()
            for i in range(2,17+1) :
                name = 'Symptom_' + str(i)
                d2 = df1.loc[df1['Disease'] == choice,name].value_counts().to_frame().reset_index()
                d1 = pd.concat([d1,d2])
            result = d1.groupby('index').sum().sum(axis=1)
            result = result.to_frame().reset_index()
            result.columns = ['symptom', 'count']
            trace1 = go.Bar(x=result['symptom'], y=result['count'])
            data = [trace1]
            layout = go.Layout(title='{}\'s Symptoms Count'.format(choice))
            fig = go.Figure(data=data, layout=layout)
            st.plotly_chart(fig)


