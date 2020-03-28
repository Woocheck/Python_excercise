import pandas as pd
import matplotlib.pyplot as plt

def plotConfirmed( listCountries ):
    
    confirmed.plot(x ='date', y=listCountries, kind = 'line')
    
    plt.title( 'Total Confirmed In Selected Countries' )
    plt.grid()
    plt.show()

def plotActivecases( listCountries ):
    
    newcases.plot(x ='date', y=listCountries, kind = 'line')
    
    plt.title( 'Daily Confirmed Cases In Selected Countries' )
    plt.grid()
    plt.show()

confirmed = pd.read_csv('https://covid.ourworldindata.org/data/ecdc/total_cases.csv')
newcases =  pd.read_csv('https://covid.ourworldindata.org/data/ecdc/new_deaths.csv')

countries = confirmed.columns
print( countries)
plotConfirmed( ['Poland', 'Germany','Italy', 'Spain','United Kingdom', 'United States', 'China'] )


