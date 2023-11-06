import streamlit as st
import pickle
import os
import pandas as pd
import sklearn
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

pastel_colors = sns.color_palette("pastel", 9)

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

    # Add space after
    st.markdown("<br>", unsafe_allow_html=True)

    # Let the user pick a set of features
    feature_set = st.selectbox("Choose a set of features", ['Set 1', 'Set 2', 'Set 3'])

    # Display the selected set of features and corresponding graph
    if feature_set == 'Set 1':
        display_set_1()
    elif feature_set == 'Set 2':
        display_set_2()
    elif feature_set == 'Set 3':
        display_set_3()

def display_set_1():
    # Display the set 1 features and graph
    st.markdown('**Danceability:**')
    st.write("Represents how suitable a track is for dancing.")
    danceability = st.slider("Example value. Range: from 0.0 (least danceable) to 1.0 (most danceable).", min_value=0.0, value=0.561)

    st.markdown('**Energy:**')
    st.write("Represents the energy of the track.")
    energy = st.slider("Example value. Range: from 0.0 (low energy) to 1.0 (high energy).", min_value=0.0, max_value=1.0, value=0.965)
         
    st.markdown('**Explicit:**')
    st.write("Represents whether the track has explicit content or not.")
    explicit = st.slider("Example value. Either 0 (represents not explicit) or 1 (represents explicit).", min_value=0, max_value=1, value = 1)
         
    st.markdown('**Mode:**')
    st.write("Represents the modality of the track. ")
    mode = st.slider("Example value. Either 0 (represents minor) or 1 (represents major).", min_value=0, max_value=1, value = 0)
         
    st.markdown('**Speechiness:**')
    st.write("Represents the presence of spoken words in the track.")
    speechiness = st.slider("Example value. Range: from 0.0 to 1.0 .", min_value=0.0, max_value=1.0, value = 0.0343)
         
    st.markdown('**Acousticness:**')
    st.write("Represents the acousticness of the track.")
    acousticness = st.slider("Example value. Range: from 0.0 (not acoustic) to 1.0 (acoustic).", min_value=0.0, max_value=1.0, value = 0.00383) 
         
    st.markdown('**Instrumentalness:**')
    st.write("Represents the instrumentalness of the track. ")
    instrumentalness = st.slider("Example value. Range: from 0.0 to 1.0.", min_value=0.0, max_value=1.0, value = 0.000007)
         
    st.markdown('**Liveness:**')
    st.write("Represents the presence of a live audience in the track. ")
    liveness = st.slider("Example value. Range: from 0.0 to 1.0.", min_value=0.0, max_value=1.0, value = 0.371)
         
    st.markdown('**Valence:**')
    st.write("Represents the musical positiveness conveyed by a track.")
    valence = st.slider("Example value. Ranges from 0.0 to 1.0.", min_value=0.0, max_value=1.0, value = 0.304)

    # Creating a sample plot for the example of popularity
    features = ['danceability', 'energy', 'explicit', 'mode', 'speechiness', 
                'acousticness', 'instrumentalness', 'liveness', 'valence']
    popularity_scores = [0.561, 0.965, 1, 0, 0.0343, 0.00383, 0.000007, 0.371, 0.304]

    # Using pastel color palette
    #pastel_colors = sns.color_palette("pastel", len(features))

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

    pass


def display_set_2():
    # Display the set 2 features and graph
    st.write("Represents the duration of the track in minutes.")
    duration_ms = st.slider("Example duration.)", min_value=0, max_value=16, step = 1, value = 2.92)

    st.markdown('**Key:**')
    st.write("Represents the key the track is in, expressed in integer notation from 0 to 11.")
    key = st.slider("Examle key. Range: https://en.wikipedia.org/wiki/Pitch_class", min_value=0, max_value=11, value = 7)

    st.markdown('**Loudness:**')
    st.write("Represents the overall loudness of the track in decibels (dB).")
    loudness = st.slider("Example loudness. Range: from -60.0 to 0.0.", min_value=-60.0, max_value=0.0, value = -3.673)

    st.markdown('**Tempo:**')
    st.write("Represents the overall estimated tempo of the track in beats per minute (BPM).")
    tempo = st.slider("Example tempo. Range: from 0 to 200.", min_value=0, max_value=200, value = 128.040)

    st.markdown('**Time-signature:**')
    st.write("Represents the number of beats in each measure.")
    followers = st.slider("Example time-signature. Range: from 3 to 7", min_value=3, max_value=7, value = 4)
    
    st.markdown('**Followers:**')
    st.write("Represents the number of followers of the artist.")
    followers = st.slider("Example followers. Range: from 0 to 115 millions.", min_value=0, max_value=115, value =26)

    # Creating a sample plot for the example of popularity
    features2 = ['duration_ms', 'key', 'loudness', 'tempo', 'time-signature', 'followers_mill']
    popularity_scores2 = [2.92, 7, -3.673, 128.040, 4, 26]

      # Using pastel color palette
    #pastel_colors = sns.color_palette("pastel", len(features))

    fig2, ax2 = plt.subplots()
    bars2 = ax2.barh(features2, popularity_scores2, color=pastel_colors)

    # Removing frame and keeping only the y-axis
    ax2.spines['top'].set_visible(False)
    ax2.spines['right'].set_visible(False)
    ax2.spines['left'].set_visible(False)
    ax2.spines['bottom'].set_visible(False)

    # Adding annotations to show the values when hovering over the bars
    for bar in bars2:
        xval = bar.get_width()
        ax.text(xval, bar.get_y() + bar.get_height() / 2, round(xval, 2), ha='left', va='center')

    st.pyplot(fig2)

    pass


def display_set_3():
    # Display the set 3 features and graph
    artist = st.text_input("artist", value = "David Guetta and Bebe Rexha" )
    genre = st.text_input("genre", value = 'pop' )

    pass

     
if __name__ == "__main__":
    display_home_page()
