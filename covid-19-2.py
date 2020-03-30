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

def plotDeathdCases( listCountries ):
    
    newdeaths.plot(x ='date', y=listCountries, kind = 'line')
    
    plt.title( 'Daily Confirmed Deaths In Selected Countries' )
    plt.grid()
    plt.show()

def plotTotalDeathdCases( listCountries ):
    
    totaldeaths.plot(x ='date', y=listCountries, kind = 'line')
    
    plt.title( 'Total Deaths In Selected Countries' )
    plt.grid()
    plt.show()

confirmed = pd.read_csv('https://covid.ourworldindata.org/data/ecdc/total_cases.csv')
newcases = pd.read_csv('https://covid.ourworldindata.org/data/ecdc/new_cases.csv')
newdeaths =  pd.read_csv('https://covid.ourworldindata.org/data/ecdc/new_deaths.csv')
totaldeaths = pd.read_csv('https://covid.ourworldindata.org/data/ecdc/total_deaths.csv')
selectedCountries = ['Poland', 'Germany','Italy', 'Spain','United Kingdom', 'United States', 'China']

plotConfirmed( selectedCountries )
plotDeathdCases( selectedCountries )
plotTotalDeathdCases( selectedCountries )
plotActivecases( selectedCountries )

