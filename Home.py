import streamlit as st
import pickle
import os
import pandas as pd
import sklearn

st.title("Hit Prediction")

st.write("""
### Project description

""")

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

# new house with fake data
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
