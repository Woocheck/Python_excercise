import pandas as pd
import pylab as plb
import matplotlib.pyplot as plt

dataPopulation = pd.read_csv('WPP2019_TotalPopulationBySex.csv')

countries =[ 'Poland', 'Nigeria', 'Germany', 'United States of America', 'Russian Federation', 'China', 'India']

for country in countries:
    MidYear = dataPopulation[ (dataPopulation['Location'] == country ) & (dataPopulation['Variant'] == 'Medium') ]
    plt.plot(MidYear['Time'],MidYear['PopTotal'], label=country)

plt.legend()
plt.grid(True)
plt.show()
