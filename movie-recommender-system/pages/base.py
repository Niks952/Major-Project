import streamlit as st
import pickle
from PIL import Image
import pandas as pd


st.title('Movie Recommendation System')
st.markdown('Made By :: **Nikhil Kumar Subham Mittal Girish Rathore Pratyush Pandey**')
# st.markdown('Nikhil Kumar ')
# st.markdown('Subham Mittal ')
# st.markdown('Girish Rathore ')
# st.markdown('Pratyush Pandey ')
image = Image.open('dsu.jpg')
st.image(image,width=125, use_column_width='never')


movie_dict = pickle.load(open('movie_dict.pkl','rb'))
similarity=pickle.load(open('similarity.pkl','rb'))
movies = pd.DataFrame(movie_dict)


def recommned(movie):
    movies_index = movies[movies['title']==movie].index[0]
    distances = similarity[movies_index]
    movies_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]

    recommended_movies=[]
    recommend_title=[]
    for i in movies_list:
         recommended_movies.append(movies.iloc[i[0]].title)
         recommend_title.append(movies.iloc[i[0]].movie_id)
    return recommended_movies


selcted_movie_name = \
     st.selectbox('What are you Netfix and Chilling to these days?',
                    movies['title'].values)

if st.button('Recommend Movies'):
     recommendations = recommned(selcted_movie_name)
     for i in recommendations:
          st.write(i)