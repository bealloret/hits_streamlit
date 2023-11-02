import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def display_additional_page():
    st.title("Set your music hit factory")
    st.write("""
    ### Here you can change the settings of your song and check if it becomes a music hit
    """)

    danceability = st.slider("Danceability", 0.0, 1.0, 0.5)
    energy = st.slider("Energy", 0.0, 1.0, 0.7)
    explicit = st.slider("Explicit", 0.0, 1.0, 0.3)
    duration_ms = st.slider("Duration (ms)", 0, 100000, 60000)
    year = st.slider("Year", 1900, 2023, 2000)
    loudness = st.slider("Loudness", -60.0, 0.0, -6.0)
    mode = st.slider("Mode", 0, 1, 0)
    speechiness = st.slider("Speechiness", 0.0, 1.0, 0.5)
    acousticness = st.slider("Acousticness", 0.0, 1.0, 0.7)
    instrumentalness = st.slider("Instrumentalness", 0.0, 1.0, 0.3)
    liveness = st.slider("Liveness", 0.0, 1.0, 0.6)
    valence = st.slider("Valence", 0.0, 1.0, 0.4)
    tempo = st.slider("Tempo", 0.0, 250.0, 120.0)
    followers = st.slider("Followers", 0, 1000000, 200000)

    # Create a DataFrame with the user inputs
    new_song = pd.DataFrame({
        'danceability': [danceability],
        'energy': [energy],
        'explicit': [explicit],
        'duration_ms': [duration_ms],
        'year': [year],
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

    st.sidebar.header("Popularity Scores")
    fig, ax = plt.subplots()
    features = list(new_song.columns)
    popularity_scores = new_song.values.flatten()

    # Using pastel color palette
    pastel_colors = sns.color_palette("pastel", len(features))

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

if __name__ == "__main__":
    display_additional_page()
