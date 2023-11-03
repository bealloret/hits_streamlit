import streamlit as st
import pickle
import os
import pandas as pd
import sklearn
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


def display_home_page():
     # Define the HTML code for the icons
    icon_html = """
        <style>
        .icon {
           display: inline-block;
           vertical-align: middle;
    }
    </style>
    <h1>
    <span class="icon">🎵</span> Welcome to the Music Hit Factory <span class="icon">⚙️</span> <span class="icon">🔩</span>
    </h1>
    """
    # Display the icons with the title using the markdown method
    st.markdown(icon_html, unsafe_allow_html=True)
    st.markdown("""
    ## Here you can test your ability to generate a music hit
    """)

    # Display the title in italic
    st.write(f"### *Look and listen to the hit*")

    # Add the image of the album from a URL with rounded corners using CSS
    st.image("https://t2.genius.com/unsafe/249x249/https%3A%2F%2Fimages.genius.com%2Ff4eacd64dc39815cf3b789fc21b3e3b2.1000x1000x1.png", 
             caption="Album Cover of I'm Good (Blue) by David Guetta and Bebe Rexha",
             width=100,
             use_column_width=False,
             clamp=False,
             )

    # Add CSS style to the image
    st.markdown(
        """
        <style>
            img {
                border-radius: 12px;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )
    
    def get_youtube_video(video_id):
        return f'''
             <iframe width="560" height="315" src="https://www.youtube.com/embed/{video_id}" 
             frameborder="0" allowfullscreen></iframe>
        '''
    video_id = '90RLzVUuXe4?si=pvocMgI6Shj_KiXZ'  # Replace with your desired YouTube video ID
    st.markdown(get_youtube_video(video_id), unsafe_allow_html=True)

     # Add space after the video
    st.markdown("<br><br>", unsafe_allow_html=True)

    # Ask the user to guess the popularity score from 0 to 100
    user_guess = st.number_input("Can you guess the popularity score (0-100) of this hit?", min_value=0, max_value=100, step=1)
    
    # Add space after the user's guess
    st.markdown("<br>", unsafe_allow_html=True)
      
    # Assuming 'popularity_score' is the variable containing the popularity score
    popularity_score = 98  # Replace with your actual popularity score

     # Display the user's guess and the actual popularity score
    if st.button("Reveal Popularity Score"):
        st.write(f"Your guess: {user_guess}")
        st.markdown("<br>", unsafe_allow_html=True)  # Add line break
        st.info(f"Actual Popularity Score: {popularity_score}")
    
    # Display the sentence 
    st.write("##### Look at the features of this song:")

    # Creating a sample plot for the example of popularity
    features = ['danceability', 'energy', 'explicit', 'duration_ms', 'year', 'key', 'loudness', 'mode', 'speechiness', 
                'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo', 'followers']
    popularity_scores = [0.561, 0.965, 1, 3, 2, 7, -3.673, 0, 0.0343, 0.00383, 0.000007, 0.371, 0.304, 128.04, 5]

    # Using pastel color palette
    pastel_colors = sns.color_palette("pastel", len(features))

    fig, ax = plt.subplots()
    bars = ax.bar(features, popularity_scores, color=pastel_colors)

    # Aligning the labels with the bars and setting smaller font size
    plt.xticks(rotation=45, ha="right", fontsize=8)
    plt.tick_params(axis='y', which='both', left=False, right=False, labelleft=False)

    # Removing frame and keeping only the x-axis
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_visible(False)

    # Adding annotations to show the values when hovering over the bars
    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, yval, round(yval, 2), va='bottom', ha='center')

    st.pyplot(fig)

    # Load model
    file_path = "trained_pipe_knn.sav"
    # Specify the full path to the file
    loaded_model = pickle.load(open(file_path, 'rb'))

    artist = st.text_input("artist")
    genre = st.text_input("genre")

    st.write("Danceability:")
    danceability = st.slider("Adjust danceability", min_value=0.0, max_value=1.0, step=0.01)


    st.write("Energy:")
    energy = st.slider("Adjust energy", min_value=0.0, max_value=1.0, step=0.01)

    st.write("Explicit:")
    explicit = st.slider("Adjust explicit", min_value=0, max_value=1, step=1)

    st.write("Duration (ms):")
    duration_ms = st.slider("Adjust duration (ms)", min_value=0, max_value=100000, step=1000)

    st.write("Year:")
    year = st.slider("Adjust year", min_value=1920, max_value=2023, step=1)

    st.write("Key:")
    key = st.slider("Adjust key", min_value=0, max_value=11, step=1)

    st.write("Loudness:")
    loudness = st.slider("Adjust loudness", min_value=-60.0, max_value=0.0, step=0.1)

    st.write("Mode:")
    mode = st.slider("Adjust mode", min_value=0, max_value=1, step=1)

    st.write("Speechiness:")
    speechiness = st.slider("Adjust speechiness", min_value=0.0, max_value=1.0, step=0.01)

    st.write("Acousticness:")
    acousticness = st.slider("Adjust acousticness", min_value=0.0, max_value=1.0, step=0.01)

    st.write("Instrumentalness:")
    instrumentalness = st.slider("Adjust instrumentalness", min_value=0.0, max_value=1.0, step=0.01)

    st.write("Liveness:")
    liveness = st.slider("Adjust liveness", min_value=0.0, max_value=1.0, step=0.01)

    st.write("Valence:")
    valence = st.slider("Adjust valence", min_value=0.0, max_value=1.0, step=0.01)

    st.write("Tempo:")
    tempo = st.slider("Adjust tempo", min_value=0, max_value=200, step=1)

    st.write("Followers:")
    followers = st.slider("Adjust followers", min_value=0, max_value=1000000, step=1000)

    # Prediction
    # Create a DataFrame with the user input
    new_song = pd.DataFrame({
        'artist': [artist],
        'genre': [genre],
        'danceability': [danceability],
        'energy': [energy],
        'explicit': [explicit],
        'duration_ms': [duration_ms],
        'year': [year],
        'key': [key],
        'loudness': [loudness],
        'mode': [mode],
        'speechiness': [speechiness],
        'acousticness': [acousticness],
        'instrumentalness': [instrumentalness],
        'liveness': [liveness],
        'valence': [valence],
        'tempo': [tempo],
        'followers': [followers]
    })

    # prediction
    prediction = loaded_model.predict(new_song)
    st.write("The success of the song is:", prediction)


if __name__ == "__main__":
    display_home_page()
