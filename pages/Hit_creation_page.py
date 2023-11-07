import streamlit as st
import pickle
import os
import pandas as pd
import matplotlib.pyplot as plt

     
def display_hit_creation_page():
     # Define the HTML code for the icons
    icon_html = """
        <style>
        .icon {
           display: inline-block;
           vertical-align: middle;
    }
    </style>
    <h1>
    <span class="icon">🎵</span> Create your music hit <span class="icon">⚙️</span> <span class="icon">🔩</span>
    </h1>
    """
    # Display the icons with the title using the markdown method
    st.markdown(icon_html, unsafe_allow_html=True)

    
    st.write("""
    ### Here you can change the settings of your song and check if it becomes a music hit
    """)

       # Create input fields for the selected features
    feature_values = {}
    for feature in features:
        if feature in ['mode', 'danceability', 'energy', 'explicit', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence']:
             feature_values[feature] = st.slider(feature, key=feature, min_value=0.0, max_value=1.0)
        else:
            if feature == 'duration_ms':
                 feature_values[feature] = st.slider(feature, key=feature, min_value=0, max_value=16)
            elif feature == 'followers':
                 feature_values[feature] = st.slider(feature, key=feature, min_value=0, max_value=115)
            elif feature == 'key':
                  feature_values[feature] = st.slider(feature, key=feature, min_value=0, max_value=11)
            elif feature == 'loudness':
                 feature_values[feature] = st.slider(feature, key=feature, min_value=-60, max_value=0)
            elif feature == 'tempo':
                 feature_values[feature] = st.slider(feature, key=feature, min_value=0, max_value=200)
            elif feature == 'time_signature':
                 feature_values[feature] = st.slider(feature, key=feature, min_value=3, max_value=7)
            elif feature in ['artist', 'genre', 'album_name']:
                 feature_values[feature] = st.text_input(f"{feature.capitalize()}", key=f"{feature}_input")
        if feature not in feature_values:
            feature_values[feature] = 0  # Replace 0 with an appropriate default value for your use case
                 


    # Load model
    file_path = "trained_pipe_knn.sav"
    loaded_model = pickle.load(open(file_path, 'rb'))

    # Create radio buttons for different feature sets
    feature_set = st.radio("Choose a feature set", ('Set 1', 'Set 2', 'Set 3'))


    # Change the labels and default values based on the selected feature set
    if feature_set == 'Set 1':
        features = ['danceability', 'energy', 'explicit', 'duration_ms', 'time_signature']
    elif feature_set == 'Set 2':
        features = ['loudness', 'mode', 'speechiness', 'acousticness', 'instrumentalness']
    elif feature_set == 'Set 3':
        features = ['liveness', 'valence', 'tempo', 'followers', 'genre', 'album_name', 'artist']
        artist = st.text_input("Artist", key="artist")
        genre = st.text_input("Genre", key="genre")
        album_name = st.text_input("Album Name", key="album_name")  # Collect input for album_name


  
    # Plot
    fig, ax = plt.subplots(figsize=(8, 5))
    colors = ['blue', 'green', 'red', 'purple', 'orange', 'yellow', 'cyan', 'magenta', 'lime', 'pink']  # Add more colors as needed
    popularity_scores = [feature_values[feature] for feature in features]

    bars = ax.bar(features, popularity_scores, color=colors[:len(features)])

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
        'key': [feature_values.get('key', 0.8)],  # Default value for key
        'loudness': [feature_values.get('loudness', 0.2)],  # Default value for loudness
        'mode': [feature_values.get('mode', 0.5)],  # Default value for mode
        'speechiness': [feature_values.get('speechiness', 0.7)],  # Default value for speechiness
        'acousticness': [feature_values.get('acousticness', 0.3)],  # Default value for acousticness
        'instrumentalness': [feature_values.get('instrumentalness', 0.6)],  # Default value for instrumentalness
        'liveness': [feature_values.get('liveness', 0.4)],  # Default value for liveness
        'valence': [feature_values.get('valence', 0.8)],  # Default value for valence
        'tempo': [feature_values.get('tempo', 0.2)],  # Default value for tempo
        'album_name':[album_name],
        'time_signature':[feature_values.get('time_signature', 4)],
        'followers': [feature_values.get('followers', 50)]  # Default value for followers
    })

    # Adjust the column names to match the names in the model file
    new_song.rename(columns={'followers': 'followers.total'}, inplace=True)
    new_song.rename(columns={'genre': 'track_genre'}, inplace=True)
    new_song.rename(columns={'artist':'artists'}, inplace=True)
    new_song['album_name'] = ''  # Add an empty column for album_name
    new_song['time_signature'] = 0  # Add a default value for time_signature


    # Display the predicted popularity
    predicted_popularity_label = loaded_model.predict(new_song)
    predicted_label_str = predicted_popularity_label[0]
    st.write(f"### Predicted popularity: {predicted_label_str}")

if __name__ == "__main__":
    display_hit_creation_page()
