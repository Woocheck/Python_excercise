import pandas as pd
import pylab as plb
import matplotlib.pyplot as plt

dataPopulation = pd.read_csv('WPP2019_TotalPopulationBySex.csv')

polandMidYear = dataPopulation[ (dataPopulation['Location'] == 'Poland') & (dataPopulation['Variant'] == 'Medium') ]
nigeriaMidYear = dataPopulation[ (dataPopulation['Location'] == 'Nigeria') & (dataPopulation['Variant'] == 'Medium') ]
usaMidYear = dataPopulation[ (dataPopulation['Location'] == 'United States of America') & (dataPopulation['Variant'] == 'Medium') ]
russiaMidYear = dataPopulation[ (dataPopulation['Location'] == 'Russian Federation') & (dataPopulation['Variant'] == 'Medium') ]

plt.plot(polandMidYear['Time'],polandMidYear['PopTotal'], label='Poland')
plt.plot(nigeriaMidYear['Time'],nigeriaMidYear['PopTotal'], label='Nigeria')
plt.plot(usaMidYear['Time'],usaMidYear['PopTotal'], label='USA')
plt.plot(russiaMidYear['Time'],russiaMidYear['PopTotal'], label='Russian Federation')

plt.legend()
plt.grid(True)
plt.show()



