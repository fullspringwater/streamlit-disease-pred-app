import joblib
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objs as go
from sklearn.metrics import confusion_matrix, accuracy_score


def run_eda():

    df1 = pd.read_csv('data/dataset.csv')

    # Disease Pie Chart
    fig1 = px.pie(df1, names='Disease',
                  title='질병 종류', width=900, height=800)
    st.plotly_chart(fig1)

    # 데이터의 NaN 값
    fig2 = px.imshow(df1.isnull(),
                     color_continuous_scale='agsunset',
                     title='NaN Data', width=800, height=500)
    st.plotly_chart(fig2)

    # 질병데이터별 증상데이터 개수
    df_disease_cnt = pd.read_csv('data/disease_cnt.csv',
                                 index_col=0)
    trace2 = go.Bar(x=df_disease_cnt['Disease'],
                    y=df_disease_cnt['Count'])
    data1 = [trace2]
    layout = go.Layout(title='Number of Symptom Data by Disease')
    fig3 = go.Figure(data=data1, layout=layout)
    st.plotly_chart(fig3)

    # 질병별 증상
    disease_list = df1['Disease'].unique().tolist()
    st.write()
    st.subheader('질병별 증상들 집계')
    choice = st.selectbox('질병 선택', disease_list)
    if st.button('결과'):
        if len(choice) != 0:
            d1 = df1.loc[df1['Disease'] == choice,
                         'Symptom_1'].value_counts().to_frame().reset_index()
            for i in range(2, 17+1):
                name = 'Symptom_' + str(i)
                d2 = df1.loc[df1['Disease'] == choice,
                             name].value_counts().to_frame().reset_index()
                d1 = pd.concat([d1, d2])
            result = d1.groupby('index').sum().sum(axis=1)
            result = result.to_frame().reset_index()
            result.columns = ['symptom', 'count']
            trace2 = go.Bar(x=result['symptom'], y=result['count'])
            data2 = [trace2]
            layout = go.Layout(title='{}\'s Symptoms Count'.format(choice))
            fig4 = go.Figure(data=data2, layout=layout)
            st.plotly_chart(fig4)

    # 테스트 모델에 대한 질병 예측 정확도
    y_test = joblib.load('data/y_test.pkl')
    y_pred = joblib.load('data/y_pred.pkl')
    accuracy = round(accuracy_score(y_test, y_pred)*100, 2)
    cm = confusion_matrix(y_test, y_pred)

    st.subheader('테스트 모델에 대한 질병 예측 정확도')
    st.subheader('{} % 입니다'.format(accuracy))

    fig5 = plt.figure(figsize=(10, 10))
    plt.title('Confusion Matrix')
    sns.heatmap(data=cm, annot=True, cmap='RdPu')
    st.pyplot(fig5)
