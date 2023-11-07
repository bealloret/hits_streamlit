import streamlit as st
from Home import display_home_page
from hit_creation_page import display_hit_creation_page
from song_similarity_search_page import display_song_similarity_search_page

def main():
    st.sidebar.title('Navigation')
    selection = st.sidebar.radio("Go to", ['Home', 'Setting page', 'Song Similarity page'], label="Choose a Page")

    if selection == 'Home':
        display_home_page()
    elif selection == 'Setting page':
        display_hit_creation_page()
    elif selection == 'Song Similarity page': 
        display_song_similarity_search_page()

if __name__ == "__main__":
    main()
