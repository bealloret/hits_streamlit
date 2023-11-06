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
             caption="I'm Good (Blue) by David Guetta and Bebe Rexha",
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
   
     # Add space
    st.markdown("<br><br>", unsafe_allow_html=True)
    # Display the sentence 
    st.write("##### Look at the features of this song:")

    # Creating a sample plot for the example of popularity
    features = ['danceability', 'energy', 'explicit', 'mode', 'speechiness', 
                'acousticness', 'instrumentalness', 'liveness', 'valence']
    popularity_scores = [0.561, 0.965, 1, 0, 0.0343, 0.00383, 0.000007, 0.371, 0.304]

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

    # Creating a sample plot for the example of popularity
    features_2 = ['duration_ms', 'key', 'loudness', 'tempo', 'time-signature']
    popularity_scores_2 = [175238, 7, -3.673, 128.040, 4]
   
   # Using pastel color palette
    pastel_colors = sns.color_palette("pastel", len(features))

    fig, ax = plt.subplots()
    bars = ax.barh(features_2, popularity_scores_2, color=pastel_colors)

  # Aligning the labels with the bars and setting smaller font size
    plt.xticks(fontsize=8)
    plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)

 # Removing frame and keeping only the y-axis
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_visible(False)

 # Adding annotations to show the values when hovering over the bars
    for bar in bars:
       xval = bar.get_width()
       ax.text(xval, bar.get_y() + bar.get_height() / 2, round(xval, 2), ha='left', va='center')

    plt.show()


    artist = st.text_input("artist")
    genre = st.text_input("genre")

    st.markdown('**Danceability:**')
    st.write("Represents how suitable a track is for dancing. Ranges from 0.0 (least danceable) to 1.0 (most danceable).")
    danceability = st.slider("Adjust danceability", min_value=0.0, max_value=1.0, step=0.01)

    st.markdown('**Energy:**')
    st.write("Represents the energy of the track. Ranges from 0.0 (low energy) to 1.0 (high energy).")
    energy = st.slider("Adjust energy", min_value=0.0, max_value=1.0, step=0.01)

    st.markdown('**Explicit:**')
    st.write("Represents whether the track has explicit content or not. 0 represents not explicit and 1 represents explicit.")
    explicit = st.slider("Adjust explicit", min_value=0, max_value=1, step=1)

    st.markdown('**Duration (ms):**')
    st.write("Represents the duration of the track in milliseconds.")
    duration_ms = st.slider("Adjust duration (ms)", min_value=0, max_value=100000, step=1000)

    st.markdown('**Year:**')
    st.write("Represents the release year of the track. Ranges from 1920 to 2023.")
    year = st.slider("Adjust year", min_value=1920, max_value=2023, step=1)

    st.markdown('**Key:**')
    st.write("Represents the key the track is in, expressed in integer notation from 0 to 11.")
    key = st.slider("Adjust key", min_value=0, max_value=11, step=1)

    st.markdown('**Loudness:**')
    st.write("Represents the overall loudness of the track in decibels (dB). Ranges from -60.0 to 0.0.")
    loudness = st.slider("Adjust loudness", min_value=-60.0, max_value=0.0, step=0.1)

    st.markdown('**Mode:**')
    st.write("Represents the modality of the track. 0 represents minor and 1 represents major.")
    mode = st.slider("Adjust mode", min_value=0, max_value=1, step=1)

    st.markdown('**Speechiness:**')
    st.write("Represents the presence of spoken words in the track. Ranges from 0.0 to 1.0.")
    speechiness = st.slider("Adjust speechiness", min_value=0.0, max_value=1.0, step=0.01)

    st.markdown('**Acousticness:**')
    st.write("Represents the acousticness of the track. Ranges from 0.0 (not acoustic) to 1.0 (acoustic).")
    acousticness = st.slider("Adjust acousticness", min_value=0.0, max_value=1.0, step=0.01)

    st.markdown('**Instrumentalness:**')
    st.write("Represents the instrumentalness of the track. Ranges from 0.0 to 1.0.")
    instrumentalness = st.slider("Adjust instrumentalness", min_value=0.0, max_value=1.0, step=0.01)

    st.markdown('**Liveness:**')
    st.write("Represents the presence of a live audience in the track. Ranges from 0.0 to 1.0.")
    liveness = st.slider("Adjust liveness", min_value=0.0, max_value=1.0, step=0.01)

    st.markdown('**Valence:**')
    st.write("Represents the musical positiveness conveyed by a track. Ranges from 0.0 to 1.0.")
    valence = st.slider("Adjust valence", min_value=0.0, max_value=1.0, step=0.01)

    st.markdown('**Tempo:**')
    st.write("Represents the overall estimated tempo of the track in beats per minute (BPM). Ranges from 0 to 200.")
    tempo = st.slider("Adjust tempo", min_value=0, max_value=200, step=1)

    st.markdown('**Followers:**')
    st.write("Represents the number of followers of the artist. Ranges from 0 to 1,000,000.")
    followers = st.slider("Adjust followers", min_value=0, max_value=1000000, step=1000)


if __name__ == "__main__":
    display_home_page()
