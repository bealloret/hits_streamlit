import streamlit as st
import pickle
import os
import pandas as pd
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer

from sklearn.preprocessing import OrdinalEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler

from sklearn.pipeline import make_pipeline
from sklearn.compose import ColumnTransformer
from sklearn.compose import make_column_transformer

# feature selection
from sklearn.feature_selection import VarianceThreshold
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import f_regression
from sklearn.feature_selection import VarianceThreshold, SelectKBest, f_regression, RFECV, SelectFromModel

# Regression models
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import RandomizedSearchCV

# Metrics
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error     #for mean_squared_error and root_mean_squared_error
from sklearn.metrics import mean_absolute_percentage_error
from sklearn.metrics import r2_score  

from sklearn import set_config
set_config(transform_output="pandas")


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
