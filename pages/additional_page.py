import streamlit as st
import pickle
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def display_additional_page():
    st.title("Set your music hit factory")
    st.write("""
    ### Here you can change the settings of your song and check if it becomes a music hit
    """)

    # Creating a sample plot for the example of popularity
    features = ['danceability', 'energy', 'explicit', 'duration_ms', 'year', 'key', 'loudness', 'mode', 'speechiness',
                'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo', 'followers']
    popularity_scores = [0.5, 0.7, 0.3, 0.6, 0.4, 0.8, 0.2, 0.5, 0.7, 0.3, 0.6, 0.4, 0.8, 0.2, 0.5]

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
            st.number_input(feature, key=feature)
        else:
            st.slider(feature, key=feature)

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
    ])

if __name__ == "__main__":
    display_additional_page()
