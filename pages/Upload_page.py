import streamlit as st

def display_upload_page():
    # Define the HTML code for the icons
    icon_html = """
    <style>
    .icon {
        display: inline-block;
        vertical-align: middle;
    }
    </style>
    <h1>
    <span class="icon">🎵</span> Upload page <span class="icon">⚙️</span> <span class="icon">🔩</span>
    </h1>
    """
    # Display the icons with the title using the markdown method
    st.markdown(icon_html, unsafe_allow_html=True)
    st.markdown("""
    ## Here you can check what are the features of your song.
    """)

    # Allow the user to upload an audio file
    st.write("### Upload Your Audio File")
    uploaded_file = st.file_uploader("Choose an audio file", type=["mp3", "wav"])

    if uploaded_file is not None:
        st.audio(uploaded_file, format='audio/mp3')

if __name__ == "__main__":
    display_upload_page()
