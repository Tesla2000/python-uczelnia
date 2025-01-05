from typing import Union

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

ratings_data = pd.read_csv(
    'ml-latest-small/ratings.csv')[['userId', 'movieId', 'rating']].to_numpy()
toy_story_data = ratings_data[np.where(ratings_data[:, 1] == 1)]


def get_movie_ratings(users: Union[float, int], movies):
    matrix = np.zeros((users, movies))
    ratings = np.zeros(users)

    ratings_index = 0  # this method assumes that data is sorted
    for i, rating in enumerate(toy_story_data):
        if i > users - 1:
            break

        current_user_id = rating[0]
        ratings[i] = rating[2]

        while ratings_index < len(ratings_data) and \
                ratings_data[ratings_index][0] < current_user_id:
            ratings_index = ratings_index + 1

        while ratings_index < len(ratings_data) and \
                ratings_data[ratings_index][0] == current_user_id:
            if ratings_data[ratings_index][1] - 2 >= 0 and \
                    ratings_data[ratings_index][1] - 2 < movies:
                matrix[i][
                    int(ratings_data[ratings_index][1] - 2)
                ] = ratings_data[ratings_index][2]
            ratings_index = ratings_index + 1

    return matrix, ratings


def plot_predictions(movies):
    X, Y = get_movie_ratings(215, movies)

    clf = LinearRegression().fit(X, Y)

    predicted = plt.scatter(
        [i for i in range(0, 215)],
        [clf.predict([X[i]]) for i in range(0, 215)],
        alpha=0.5)
    actual = plt.scatter(
        [i for i in range(0, 215)],
        [Y[i] for i in range(0, 215)],
        alpha=0.5,
        c='r')
    plt.legend((predicted, actual), ('Predicted values', 'Actual values'))
    plt.title(f"Predictions for {movies} movies")
    plt.show()
    plt.clf()


def show_diffs(test_group, movies):
    full_group = 215

    X, Y = get_movie_ratings(full_group, movies)
    y = Y[0:test_group]
    x = X[0:test_group]

    clf = LinearRegression().fit(x, y)

    for i in range(test_group, full_group):
        print(f"{i}: {clf.predict([X[i]])}, actual: {Y[i]}")


for m in [10, 1000, 10000]:
    plot_predictions(m)

for m in [10, 100, 200, 500, 1000, 10000]:
    print(f"PREDICTIONS FOR {m} MOVIES:")
    show_diffs(200, m)
