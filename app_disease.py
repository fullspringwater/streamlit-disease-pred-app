import streamlit as st
import pandas as pd
import numpy as np
import joblib
def run_disease() :
    st.subheader('증상을 선택하시면 질병을 예측합니다.')
    df = pd.read_csv('data/new_symptom_weight.csv', index_col= 0)
    df2 = pd.read_csv('data/disease_disc_prec.csv', index_col=0)
    
    symp_list = df['Symptom'].values.tolist()
    symp_choice = st.multiselect('증상을 선택하시오( 최대 17개 )',
                                    symp_list)
                                    
    classifier = joblib.load('data/classifier.pkl')                                
    st.text('선택 증상 개수 : {}'.format(len(symp_choice)))
    if st.button('예상 질병 보기') :
        if len(symp_choice) == 0 :
            st.warning('증상을 선택하세요')
        elif len(symp_choice) <= 17 :
            result_list = np.zeros(17)
            # 선택한 증상들을 리스트에 넣는다.
            j = 0
            for i in symp_choice :
                result_list[j] = int(df.loc[df['Symptom']==i, 
                                'weight'])
                j = j+1

            # 데이터 shape 맞추고 predict
            new_data = np.array(result_list)
            new_data = new_data.reshape(1,17)
            new_pred = classifier.predict(new_data)[0]
            
            st.subheader('당신의 예상 질병은 {} 입니다.'.format(new_pred))
            
            # Description 추출
            st.subheader('{} 에 대한 설명'.format(new_pred))
            desc = df2.loc[df2['Disease'] == new_pred,
                            'Description'].iloc[0,]
            st.write(desc)

            # precaution 추출
            st.subheader('예방법')
            precaution = df2.loc[df2['Disease'] == new_pred,
                    'Precaution_1' :].values.flatten().tolist()
            for i in range(len(precaution)) :
                if precaution[i] != '0' :
                    st.write(precaution[i])                  
        else :
            st.warning('최대 17개까지 선택가능합니다.')

        
            