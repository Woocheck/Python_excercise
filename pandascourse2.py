import pandas as pd

movie = pd.read_csv('http://bit.ly/imdbratings')

print(movie.describe())
movie.