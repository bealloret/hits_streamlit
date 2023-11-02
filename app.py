# app.py

import streamlit as st
from home_page import main as home_page_main
from additional_page import additional_page_main

PAGES = {
    "Home": home_page_main,
    "Hit generation": make the music a hit,
}

def main():
    st.sidebar.title('Navigation')
    selection = st.sidebar.radio("Go to", list(PAGES.keys()))
    page = PAGES[selection]
    page()

if __name__ == "__main__":
    main()
