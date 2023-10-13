import streamlit as st
import pandas as pd
import pickle
import requests

def fetch_poster(movie_id):
    print(movie_id)
    api_key = "b6e49ba112557efd24ff406db81a370a"
    url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US'
    response = requests.get(url)
    # response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=b6e49ba112557efd24ff406db81a370a&language=en-US'.format(movie_id))
    data = response.json()
    print(data)

    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distance = similarity[movie_index]
    movie_list = sorted(list(enumerate(distance)),reverse=True,key=lambda x:x[1])[1:6]
    
    recommended_movies=[]
    recommended_movies_posters=[]
    for i in movie_list:
        movie_id = [i[0]]
        #fatch poster
        print(movie_id)

        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))        
    return recommended_movies, recommended_movies_posters

movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    'Select a movie',
    movies['title'].values)

if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)