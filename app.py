import streamlit as st
from streamlit_option_menu import option_menu
from app_disease import run_disease
from app_eda import run_eda
from app_home import run_home

def main() :
    st.set_page_config(layout="wide")
    st.title('증상으로 질병 예측하기 프로젝트')
    menu = ['Home', 'EDA', 'Disease Pred']
    with st.sidebar:
        st.sidebar.image("data/disease.jpg", use_column_width=True)
        choose = option_menu("Menu", menu,
                            icons=['house', 'graph-up', 'book'],
                            menu_icon="app-indicator", default_index=0,
                            styles={
            "container": {"padding": "5!important", "background-color": "#44475A5"},
            "icon": {"color": "orange", "font-size": "25px"}, 
            "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#BD93F9"},
            "nav-link-selected": {"background-color": "#02ab21"},
        }
        )
    if choose == menu[0] :
        run_home()
    elif choose == menu[1] :
        run_eda()
    elif choose == menu[2] :
        run_disease()

if __name__=='__main__' :
    main()