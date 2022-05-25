import streamlit as st
import pandas as pd
import numpy as np
import joblib
def run_disease() :
    st.subheader('증상을 선택하시면 질병을 예측해줍니다.')
    df = pd.read_csv('data/Symptom-severity.csv')
    st.dataframe(df)

    symp_list = df['Symptom'].values.tolist()
    symp_w_list = df['weight'].values.tolist()
    result_list = np.zeros(17)
    symp_choice = st.multiselect('증상을 선택하시오( 최대 17개 )',
                                    symp_list)
    st.text('spymp_choice의 길이 {}'.format(len(symp_choice)))
    if st.button('예상 질병 보기') :
        if len(symp_choice) <= 17 :
            for i in range(len(symp_choice)) :
                result_list[i] = df.loc[df['Symptom']==symp_choice[i], 
                                'weight'][0]

        
            