import pandas as pd

chipotleData = pd.read_table( 'chipotle.tsv')
print( chipotleData )

user_cols = ['User_ID', 'Age', 'Gender', 'Zip_code']
movieData = pd.read_table( 'http://bit.ly/movieusers', sep='|', header=None, names=user_cols)
print( movieData )

ufo = pd.read_csv( 'ufo.csv')

type(ufo)
print( ufo.head() )