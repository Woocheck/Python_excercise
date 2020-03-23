import pandas as pd

drinks = pd.read_csv('http://bit.ly/drinksbycountry')

print( drinks.head())

print( drinks.columns )

drinksNoHead = pd.read_table( 'http://bit.ly/movieusers', header = None, sep='|')
print( drinksNoHead.head() )