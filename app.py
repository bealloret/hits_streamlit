import streamlit as st
from Home import display_home_page
from hit_creation_page import display_hit_creation_page

def main():
    st.sidebar.title('Navigation')
    selection = st.sidebar.radio("Go to", ['Home', 'Setting page'], label="Choose a Page")

    if selection == 'Home':
        display_home_page()
    elif selection == 'Setting page':
        display_hit_creation_page()

if __name__ == "__main__":
    main()
