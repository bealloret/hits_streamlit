import streamlit as st
import pickle
import os
import pandas as pd
import matplotlib.pyplot as plt

def display_additional_page():
    st.title("Set your music hit factory")
    st.write("""
    ### Here you can change the settings of your song and check if it becomes a music hit
    """)

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
    feature_values = {}
    for feature in features:
        if feature == 'year' or feature == 'key' or feature == 'mode':
            feature_values[feature] = st.number_input(feature, key=feature)
        else:
            feature_values[feature] = st.slider(feature, key=feature)

    # Plot
    fig, ax = plt.subplots(figsize=(8, 5))
    colors = ['blue', 'green', 'red', 'purple', 'orange']
    popularity_scores = [feature_values[feature] for feature in features]

    bars = ax.bar(features, popularity_scores, color=colors)

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
        'danceability': [feature_values.get('danceability', 0.5)],  # Default value for danceability
        'energy': [feature_values.get('energy', 0.7)],  # Default value for energy
        'explicit': [feature_values.get('explicit', 0.3)],  # Default value for explicit
        'duration_ms': [feature_values.get('duration_ms', 0.6)],  # Default value for duration_ms
        'year': [feature_values.get('year', 0.4)],  # Default value for year
        'key': [feature_values.get('key', 0.8)],  # Default value for key
        'loudness': [feature_values.get('loudness', 0.2)],  # Default value for loudness
        'mode': [feature_values.get('mode', 0.5)],  # Default value for mode
        'speechiness': [feature_values.get('speechiness', 0.7)],  # Default value for speechiness
        'acousticness': [feature_values.get('acousticness', 0.3)],  # Default value for acousticness
        'instrumentalness': [feature_values.get('instrumentalness', 0.6)],  # Default value for instrumentalness
        'liveness': [feature_values.get('liveness', 0.4)],  # Default value for liveness
        'valence': [feature_values.get('valence', 0.8)],  # Default value for valence
        'tempo': [feature_values.get('tempo', 0.2)],  # Default value for tempo
        'followers': [feature_values.get('followers', 0.5)]  # Default value for followers
    })

    # Display the predicted popularity
    predicted_popularity = loaded_model.predict(new_song)
    st.write(f"Predicted popularity: {predicted_popularity}")

if __name__ == "__main__":
    display_additional_page()
