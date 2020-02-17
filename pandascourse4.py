import pandas as pd

dataPopulation = pd.read_csv('/home/user/workspace_python/pandas/Python_excercise/PopulationUN.csv')

print( dataPopulation.head( 10 ) )
print( dataPopulation.columns )
print( dataPopulation[u'Unnamed: 4'] )


