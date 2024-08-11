# -*- coding: utf-8 -*-
"""ybi.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1bd6_7ucMjVRJnXc6-R6RW-gEzclAqeMi

PROJECT : Movie Recommendation System

OBJECTIVE :**Recommender System** is a system that seeks to predict or filter preferences according to the user's choices. Recommender systems are utilized in a variety of areas including movies, music, news, books, research articles, search queries, social tags, and products in general. Recommender systems produce a list of recommendations in any of the two ways -

Collaborative filtering: Collaborative filtering approaches build a model from the user's past behavior (i.e. Items purchased or searched by the user) as well as similar decisions made by other users. This model is then used to predict items (or ratings for items) that users may have an interest in.

Content-based filtering: Content-based filtering approaches uses a series of discrete characteristics of an item in order to recommend additional items with similar properties. Content-based filtering methods are totally based on a description of the item and a profile of the user's preferences. It recommends items based on the user's past preferences. Let's develop a basic recommendation system using Python and Pandas.

Let's develop a basic recommendation system by suggesting items that are most similar to a particular item, in this case, movies. It just tells what movies/items are most similar to the user's movie choice
"""

import pandas as pd
import numpy as np
# import dataset
df = pd.read_csv('https://raw.githubusercontent.com/YBI-Foundation/Dataset/main/Movies%20Recommendation.csv')
df.head()

df.info()

df.shape

df.columns

# Get feature Selection
df_features = df[['Movie_Genre','Movie_Keywords','Movie_Tagline','Movie_Cast','Movie_Director']].fillna('')

df_features.shape

df_features

x = df_features['Movie_Genre'] + ' ' + df_features['Movie_Keywords'] + ' ' + df_features['Movie_Tagline'] + ' ' + df_features['Movie_Cast'] + ' ' + df_features['Movie_Director']

x

x.shape

#Get Feature Text Conversion to Tokens
from sklearn.feature_extraction.text import TfidfVectorizer
tfidf = TfidfVectorizer()
X = tfidf.fit_transform(x)
X.shape

print(X)

#Get Similaity Score using Cosine Similarity
from sklearn.metrics.pairwise import cosine_similarity
Similarity_Score = cosine_similarity(X)
Similarity_Score

Similarity_Score.shape

"""Get Movie Name as Input from User and Validate for Closest Spelling"""

Favourite_Movie_Name = input('Enter your favourite movie name : ')

All_Movies_Title_List = df['Movie_Title'].tolist()
import difflib
Movie_Recommendation = difflib.get_close_matches(Favourite_Movie_Name, All_Movies_Title_List)
print(Movie_Recommendation)

Close_Match = Movie_Recommendation[0]
print(Close_Match)

Index_of_Close_Match_Movie = df[df.Movie_Title == Close_Match]['Movie_ID'].values[0]
print(Index_of_Close_Match_Movie)

# getting a list of similar movies
Recommendation_score = list(enumerate(Similarity_Score[Index_of_Close_Match_Movie]))
print(Recommendation_score)

len(Recommendation_score)

"""Get All Movies Sort Based on Recommendation Score wrt Favourite Movie"""

# sorting the movies based on their similarity score
Sorted_Similar_Movies = sorted(Recommendation_score, key = lambda x:x[1], reverse = True)
print(Sorted_Similar_Movies)

# print the name of similar movies based on the index
print('Top 30 Movies Suggested for You : \n')

i = 1

for movie in Sorted_Similar_Movies:
  index = movie[0]
  title_from_index = df[df.index==index]['Movie_Title'].values[0]
  if (i<31):
    print(i, '.',title_from_index)
    i+=1

"""Top 10 Movie Recommendation System"""

Movie_Name = input(' Enter your favourite movie name : ')

list_of_all_titles = df['Movie_Title'].tolist()

Find_Close_Match = difflib.get_close_matches(Movie_Name, list_of_all_titles)

Close_Match = Find_Close_Match[0]

Index_of_Movie = df[df.Movie_Title == Close_Match]['Movie_ID'].values[0]

Recommendation_score = list(enumerate(Similarity_Score[Index_of_Movie]))

Sorted_Similar_Movies = sorted(Recommendation_score, key = lambda x:x[1], reverse = True)

print('Top 10 Movies Suggested for You : \n')

i = 1

for movie in Sorted_Similar_Movies:
  index = movie[0]
  title_from_index = df[df.Movie_ID==index]['Movie_Title'].values
  if (i<11):
    print(i, '.',title_from_index)
    i+=1

"""Explaination :

My project is about movie recommendation system.It's about recommending a movie and what type of movie do user want.There is a database where the movie names will store which are going to recommend to the user.
The Main theme of this project is to save the time of the user in searching a movie which the user likes...

There's another database where all the movies will store, from which a user can easily access movies.
"""