import streamlit as st
from Home import display_home_page
from additional_page import display_additional_page

def main():
    st.sidebar.title('Navigation')
    selection = st.sidebar.radio("Go to", ['Home', 'Set page'])

    if selection == 'Home':
        display_home_page()
    elif selection == 'Set page':
        display_additional_page()

if __name__ == "__main__":
    main()
