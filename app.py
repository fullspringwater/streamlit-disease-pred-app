import streamlit as st

from app_disease import run_disease
from app_eda import run_eda

def main() :
    menu = ['Home', 'EDA', 'Disease Pred']
    choice_menu = st.sidebar.selectbox('메뉴 선택', menu)

    if choice_menu == menu[0] :
        pass
    elif choice_menu == menu[1] :
        run_eda()
    elif choice_menu == menu[2] :
        run_disease()
if __name__=='__main__' :
    main()