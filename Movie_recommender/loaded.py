# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 23:13:40 2020

@author: Sarbajit
"""

import joblib
sim_matrix = joblib.load('movie_rec.pkl')
import pandas as pd
#load the data
movie_data = pd.read_csv('movies_metadata.csv', low_memory=False)
indices = pd.Series(movie_data.index, index=movie_data['title']).drop_duplicates()
indices[:10]
def content_based_recommender(title, sim_scores=sim_matrix):
    idx = indices[title]
    sim_scores = list(enumerate(sim_matrix[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]
    movie_indices = [i[0] for i in sim_scores]
    return movie_data['title'].iloc[movie_indices]
print(content_based_recommender('Toy Story'))
