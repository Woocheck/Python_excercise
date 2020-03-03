import pandas as pd

drinksData = pd.read_csv('http://bit.ly/drinksbycountry')

print( drinksData.head() )


print( drinksData.dtypes )

drinksData['beer_servings'] = drinksData['beer_servings'].astype(float)

print( drinksData.dtypes )