import streamlit as st
import pickle
import pandas as pd
 
new_df = pickle.load(open('df.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))
titles = new_df['title']   # use Series instead of DataFrame

def recommend(movie):
    index = int(new_df[new_df['title'] == movie].index[0])
    similar = sorted(enumerate(similarity[index]), reverse=True, key=lambda x: x[1])[1:7]  # skip the same movie
    
    movies_titles = []
    movies_posters = []
    
    for i in similar:
        movies_titles.append(new_df.iloc[i[0]].title)
        movies_posters.append(new_df.iloc[i[0]].poster)
        
    return movies_titles, movies_posters


st.header('Movie Recommender System')

movie = st.selectbox('Select movie', titles)

if st.button('Recommend'):
    names, posters = recommend(movie)
    
    # Display 3 images in a row
    cols = st.columns(3)
    for idx, (name, poster) in enumerate(zip(names, posters)):
        with cols[idx % 3]:   # cycle through 3 columns
            st.text(name)
            st.image(poster, use_container_width=True)
