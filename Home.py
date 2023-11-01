import streamlit as st
import pickle
import os
import pandas as pd
import sklearn
import matplotlib.pyplot as plt

st.title("Welcome to the music hit factory")

st.write("""
### Here you can test your hability to generate a music hit

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

# load model
file_path = file_path = "trained_pipe_knn.sav"
 # Specify the full path to the file
loaded_model = pickle.load(open(file_path, 'rb'))

artist = st.text_input("artits")
genre = st.text_input("genre")
danceability = st.number_input("danceability")
energy = st.number_input("energy")
explicit = st.number_input("explicit")
duration_ms = st.number_input("duration_ms")
year = st.number_input("year")
key = st.number_input("key")
loudness = st.number_input("loudness")
mode = st.number_input("mode")
speechiness = st.number_input("speechiness")
acousticness= st.number_input("acousticness")
instrumentalness =  st.number_input("instrumentalness")
liveness = st.number_input("liveness")
valence = st.number_input("valence")
tempo = st.number_input("tempo")
followers = st.number_input("followers")

# Create a DataFrame with the user input
import pandas as pd
new_song = pd.DataFrame({
    'artist':[artist],
    'genre': [genre],
    'danceability':[danceability],
    'energy':[energy],
    'explicit':[explicit],
    'duration_ms': [duration_ms],
    'year':[year],
    'key':[key],
    'loudness':[loudness],
    'mode':[mode],
    'speechiness':[speechiness],
    'acousticness':[acousticness],
    'instrumentalness':[instrumentalness],
    'liveness':[liveness],
    'valence':[valence],
    'tempo':[tempo],
    'followers':[followers]
})

# prediction
prediction = loaded_model.predict(new_song)
st.write("The success of the song is:", prediction)
