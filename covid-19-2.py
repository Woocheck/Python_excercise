import pandas as pd
import matplotlib.pyplot as plt

def plotCases( listCountries, data, diagramTitle ):
    
    data.plot(x ='date', y=listCountries, kind = 'line')
    
    plt.title( diagramTitle )
    plt.grid()
    plt.show()

confirmed = pd.read_csv('https://covid.ourworldindata.org/data/ecdc/total_cases.csv')
newcases = pd.read_csv('https://covid.ourworldindata.org/data/ecdc/new_cases.csv')
newdeaths =  pd.read_csv('https://covid.ourworldindata.org/data/ecdc/new_deaths.csv')
totaldeaths = pd.read_csv('https://covid.ourworldindata.org/data/ecdc/total_deaths.csv')
selectedCountries = ['Poland', 'Germany','Italy', 'Spain','United Kingdom', 'United States', 'China']

plotCases( selectedCountries, confirmed,'Total Confirmed In Selected Countries')
plotCases( selectedCountries, newdeaths, 'Daily Confirmed Deaths In Selected Countries' )
plotCases( selectedCountries, totaldeaths, 'Total Deaths In Selected Countries' )
plotCases( selectedCountries, newcases, 'Daily Confirmed Cases In Selected Countries' )

