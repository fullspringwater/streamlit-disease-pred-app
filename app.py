import streamlit as st

from app_disease import run_disease

def main() :
    menu = ['Home', 'EDA', 'Disease Pred']
    choice_menu = st.sidebar.selectbox('메뉴 선택', menu)

    if choice_menu == menu[0] :
        pass
    elif choice_menu == menu[1] :
        pass
    elif choice_menu == menu[2] :
        run_disease()
if __name__=='__main__' :
    main()