import streamlit as st
from streamlit_option_menu import option_menu
from app_disease import run_disease
from app_eda import run_eda
from app_home import run_home

def main() :
    st.title('증상으로 질병 예측하기 프로젝트')
    menu = ['Home', 'EDA', 'Disease Pred']
    st.sidebar.image("data/disease.jpg", use_column_width=True)
    choice_menu = st.sidebar.selectbox('메뉴 선택', menu)

    if choice_menu == menu[0] :
        run_home()
    elif choice_menu == menu[1] :
        run_eda()
    elif choice_menu == menu[2] :
        run_disease()
    st.markdown(
                """
            <style>
            .sidebar .sidebar-content {
                background-image: linear-gradient(#2e7bcf,#2e7bcf);
                color: white;
            }
            </style>
            """,
    unsafe_allow_html=True,
    )
if __name__=='__main__' :
    main()