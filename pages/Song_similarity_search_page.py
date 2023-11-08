import pandas as pd
import streamlit as st
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.metrics import euclidean_distances
import pickle


def calculate_similarities(data, input_values):
    # Define numerical and categorical features
    numerical_features = ['duration_ms', 'popularity', 'danceability', 'energy', 'loudness', 'speechiness', 'acousticness', 
                          'instrumentalness', 'liveness', 'valence',
                         'tempo', 'followers.total']
    categorical_features = ['key', 'mode', 'track_genre', 'explicit', 'time_signature']

    # Create pipelines for numerical and categorical data
    numerical_pipeline = Pipeline([
        ('imputer', SimpleImputer(strategy='mean')),
        ('scaler', StandardScaler())
    ])

    categorical_pipeline = Pipeline([
        ('imputer', SimpleImputer(strategy='most_frequent')),
        ('onehot', OneHotEncoder(handle_unknown='ignore', sparse_output = False))
    ])

    # Combine the numerical and categorical pipelines into a single column transformer
    preprocessor = ColumnTransformer([
        ('num', numerical_pipeline, numerical_features),
        ('cat', categorical_pipeline, categorical_features)
    ])
    
    try:
        with open('preprocessor.pkl', 'rb') as file:
            preprocessor = pickle.load(file)
    except FileNotFoundError:
        preprocessor = preprocessor.fit(data)
        with open('preprocessor.pkl', 'wb') as file:
            pickle.dump(preprocessor, file)

    dataset_processed = preprocessor.transform(data)
    input_values_processed = preprocessor.transform(input_values)
    
    # Calculate similarities using Euclidean distances
    similarities = euclidean_distances(dataset_processed, input_values_processed)
    
      # Convert the 2D similarity array to a 1D Series
    similarities_series = pd.Series(similarities.flatten())
    
    # Create a new DataFrame to store the dataset with similarities
    dataset_similarities = pd.concat([dataset_df.reset_index(drop=True), similarities_series], axis=1)
    
    return dataset_similarities.head(5)

def display_song_similarity_search_page():
    st.title("Song Similarity Search")

# Example data (replace this with your dataset)
data = pd.DataFrame()

# Create Streamlit app
st.write("Please input the features of the song to find similar songs.")

# Input fields for each feature
numerical_features = ['duration_ms', 'popularity', 'danceability', 'energy', 'loudness', 'popularity', 'speechiness',
                      'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo', 'followers.total']
categorical_features = ['key', 'mode', 'track_genre', 'explicit', 'time_signature']

input_values = {}

for feature in numerical_features:
    if feature in ['danceability', 'energy', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence']:
        input_values[feature] = st.slider(f"Enter {feature} value", key=f"{feature}_slider", min_value=0.0, max_value=1.0)
    else:
        if feature == 'duration_ms':
            input_values[feature] = st.slider(f"Enter {feature} value", key=f"{feature}_slider", min_value=0, max_value=16)
        elif feature == 'followers.total':
            input_values[feature] = st.slider(f"Enter {feature} value", key=f"{feature}_slider", min_value=0, max_value=115)
        elif feature == 'loudness':
            input_values[feature] = st.slider(f"Enter {feature} value", key=f"{feature}_slider", min_value=-60, max_value=0)
        elif feature == 'tempo':
            input_values[feature] = st.slider(f"Enter {feature} value", key=f"{feature}_slider", min_value=0, max_value=200)
        elif feature == 'popularity':
            input_values[feature] = st.slider(f"Enter {feature} value", key=f"{feature}_slider", min_value=0, max_value=100)
        elif feature == 'followers.total':
            input_values[feature] = st.slider(f"Enter {feature} value", key=f"{feature}_slider", min_value=0, max_value=150000000)

for feature in categorical_features:
    if feature == 'track_genre':
        input_values[feature] = st.text_input(f"Enter {feature} value", key=f"{feature}_input")
    elif feature == 'key':
        input_values[feature] = st.slider(f"Enter {feature} value", key=f"{feature}_slider", min_value=0, max_value=11)
    elif feature == 'mode' or feature == 'explicit':
        input_values[feature] = st.slider(f"Enter {feature} value", key=f"{feature}_slider", min_value=0, max_value=1)
    elif feature == 'time_signature':
        input_values[feature] = st.slider(f"Enter {feature} value", key=f"{feature}_slider", min_value=3, max_value=7)

      
# Convert the input values to a DataFrame
input_df = pd.DataFrame([input_values])

# Process the data and get the similar songs
similar_songs = calculate_similarities(data, input_df)

# Display the results
st.write("Top 5 similar songs:")
st.write(similar_songs)

if __name__ == "__main__":
    display_song_similarity_search_page()
