import streamlit as st
import pickle
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def display_additional_page():
    danceability = 0.5  # Default value for danceability
    energy = 0.7  # Default value for energy
    explicit = 0.3  # Default value for explicit
    duration_ms = 0.6  # Default value for duration_ms
    year = 0.4  # Default value for year
    loudness = 0.8  # Default value for loudness
    mode = 0.2  # Default value for mode
    speechiness = 0.5  # Default value for speechiness
    acousticness = 0.7  # Default value for acousticness
    instrumentalness = 0.3  # Default value for instrumentalness
    liveness = 0.6  # Default value for liveness
    valence = 0.4  # Default value for valence
    tempo = 0.8  # Default value for tempo
    followers = 0.2  # Default value for followers
    key = 0  # Default value for key

    st.title("Set your music hit factory")
    st.write("""
    ### Here you can change the settings of your song and check if it becomes a music hit
    """)

    # Creating a sample plot for the example of popularity
    features = ['danceability', 'energy', 'explicit', 'duration_ms', 'year', 'key', 'loudness', 'mode', 'speechiness',
                'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo', 'followers']
    popularity_scores = [danceability, energy, explicit, duration_ms, year, key, loudness, mode, speechiness,
                         acousticness, instrumentalness, liveness, valence, tempo, followers]

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
    loaded_model = pickle.load(open(file_path, 'rb'))

    # Create radio buttons for different feature sets
    feature_set = st.radio("Choose a feature set", ('Set 1', 'Set 2', 'Set 3'))

    artist = st.text_input("artist")
    genre = st.text_input("genre")

    # Change the labels and default values based on the selected feature set
    if feature_set == 'Set 1':
        features = ['danceability', 'energy', 'explicit', 'duration_ms', 'year']
    elif feature_set == 'Set 2':
        features = ['loudness', 'mode', 'speechiness', 'acousticness', 'instrumentalness']
    elif feature_set == 'Set 3':
        features = ['liveness', 'valence', 'tempo', 'followers']

    # Create input fields for the selected features
    for feature in features:
        if feature == 'year' or feature == 'key' or feature == 'mode':
            value = st.slider(feature, key=feature, value=0, min_value=0, max_value=100, step=1)
        else:
            value = st.slider(feature, key=feature, value=0.5, min_value=0.0, max_value=1.0, step=0.01)
        popularity_scores[features.index(feature)] = value

    # Recreate the bar plot with updated values
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

    # Create a DataFrame with the user inputs
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

if __name__ == "__main__":
    display_additional_page()
