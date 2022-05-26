import streamlit as st

from app_disease import run_disease
from app_eda import run_eda
from app_home import run_home

def main() :
    st.title('증상으로 질병 예측하기 프로젝트')
    menu = ['Home', 'EDA', 'Disease Pred']
    choice_menu = st.sidebar.selectbox('메뉴 선택', menu)

    if choice_menu == menu[0] :
        run_home()
    elif choice_menu == menu[1] :
        run_eda()
    elif choice_menu == menu[2] :
        run_disease()
if __name__=='__main__' :
    main()