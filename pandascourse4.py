import pandas as pd
import pylab as plb
import matplotlib.pyplot as plt

dataPopulation = pd.read_csv('/home/user/workspace_python/pandas/Python_excercise/WPP2019_TotalPopulationBySex.csv')

worldMidYear = dataPopulation[ dataPopulation['Location'] == 'Poland' ]

print( worldMidYear[['Time', 'Location', 'PopTotal']] )



