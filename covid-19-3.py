import pandas as pd
import matplotlib.pyplot as plt

def plotCases( row, column, listCountries, data, diagramTitle ):
    
    data.plot(ax=axes[row,column], x ='date', y=listCountries, kind = 'line' )
        
    plt.title( diagramTitle )
    

confirmed = pd.read_csv('https://covid.ourworldindata.org/data/ecdc/total_cases.csv')
newcases = pd.read_csv('https://covid.ourworldindata.org/data/ecdc/new_cases.csv')
newdeaths =  pd.read_csv('https://covid.ourworldindata.org/data/ecdc/new_deaths.csv')
totaldeaths = pd.read_csv('https://covid.ourworldindata.org/data/ecdc/total_deaths.csv')

selectedCountries = ['Poland', 'Germany','Italy', 'Spain','United Kingdom', 'United States', 'China','Czech Republic']

fig, axes = plt.subplots(nrows=2, ncols=2)
plotCases( 0, 0, selectedCountries, confirmed,'Total Confirmed In Selected Countries')
plotCases( 0, 1, selectedCountries, newcases, 'Daily Confirmed Cases In Selected Countries' )
plotCases( 1, 0, selectedCountries, newdeaths, 'Daily Confirmed Deaths In Selected Countries' )
plotCases( 1, 1, selectedCountries, totaldeaths, 'Total Deaths In Selected Countries' )

plt.grid()
plt.show()
