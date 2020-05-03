from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

ratings_data = pd.read_csv('ml-latest-small/ratings.csv')
movies_data = pd.read_csv('ml-latest-small/movies.csv')

ratings_data = ratings_data[(ratings_data.movieId < 10000)]
movies_data = movies_data[(movies_data.movieId < 10000)]

users = {
    user: index
    for index, user in enumerate(set(ratings_data['userId']))
}

preferences_matrix = np.zeros(
    (len(users), 1 + max(set(ratings_data['movieId'])))
)

for r in ratings_data.itertuples():
    preferences_matrix[users[int(r.userId)]][int(r.movieId)] = r.rating

preferences_matrix = np.nan_to_num(
    preferences_matrix/np.nan_to_num(
        np.linalg.norm(preferences_matrix, axis=0)
    )
)

custom_ratings = np.zeros((preferences_matrix.shape[1], 1))
custom_ratings[123] = 2
custom_ratings[321] = 1
custom_ratings[456] = 3
custom_ratings[654] = 7

custom_ratings = custom_ratings/np.linalg.norm(custom_ratings)
z = np.dot(preferences_matrix, custom_ratings)
z = z/np.linalg.norm(z)
out = np.dot(preferences_matrix.T, z)
ranked = sorted(
    [
        (pref, movies_data[(movies_data['movieId'] == i)])
        for i, pref in enumerate(out)
    ],
    key=lambda el: el[0],
    reverse=True
)

for i, movie in enumerate(ranked[:10]):
    print(f"{i + 1}. {movie[1]['title'].to_string(index=False)} {movie[0]}")
