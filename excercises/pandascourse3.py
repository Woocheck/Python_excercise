import pandas as pd

dataMovie = pd.read_csv('http://bit.ly/imdbratings')

print( dataMovie.head( 10 ) )
print( dataMovie['title'].sort_values(ascending=False).head() )
print( dataMovie.sort_values(['title'],ascending=False).head() )

print( dataMovie[ (dataMovie['duration'] >= 200) & (dataMovie['star_rating'] >= 8.5 ) ].head())



