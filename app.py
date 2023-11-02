# app.py

import streamlit as st
from home_page import display_home_page
from additional_page import display_additional_page

def main():
    st.sidebar.title('Navigation')
    selection = st.sidebar.radio("Go to", ['Home Page', 'Set page'])

    if selection == 'Home Page':
        display_home_page()
    elif selection == 'Additional Page':
        display_additional_page()

if __name__ == "__main__":
    main()
