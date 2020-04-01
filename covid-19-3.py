import pandas as pd
import matplotlib.pyplot as plt

def plotCases( nr, listCountries, data, diagramTitle ):
    
    plt.subplot(2, 2, nr)
    data.plot(x ='date', y=listCountries, kind = 'line')
    
    #plt.title( diagramTitle )
    plt.grid()
    

confirmed = pd.read_csv('https://covid.ourworldindata.org/data/ecdc/total_cases.csv')
newcases = pd.read_csv('https://covid.ourworldindata.org/data/ecdc/new_cases.csv')
newdeaths =  pd.read_csv('https://covid.ourworldindata.org/data/ecdc/new_deaths.csv')
totaldeaths = pd.read_csv('https://covid.ourworldindata.org/data/ecdc/total_deaths.csv')

selectedCountries = ['Poland', 'Germany','Italy', 'Spain','United Kingdom', 'United States', 'China','Czech Republic']

fig = plt.figure()

plt.subplot(2, 2, 1)
confirmed.plot( x ='date', y=selectedCountries ) #,'Total Confirmed In Selected Countries')
plt.subplot(2, 2, 2)
newcases.plot( x ='date', y=selectedCountries )# 'Daily Confirmed Cases In Selected Countries' )
plt.subplot(2, 2, 3)
newdeaths.plot( x ='date', y=selectedCountries )# 'Daily Confirmed Deaths In Selected Countries' )
plt.subplot(2, 2, 4)
totaldeaths.plot( x ='date', y=selectedCountries )# 'Total Deaths In Selected Countries' )

plt.show()
