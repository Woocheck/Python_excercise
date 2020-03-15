import pandas as pd
import matplotlib.pyplot as plt

def plotConfirmed( listCountries ):
    
    selsctedCountries = confirmed[ confirmed['Country/Region'].isin(listCountries) ].transpose()
    selsctedCountries.columns = selsctedCountries.iloc[1]
    selsctedCountries[4:].plot()
    
    plt.title( 'Total Confirmed In Selected Countries' )
    plt.grid()
    plt.show()

confirmed = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv')

countries = confirmed['Country/Region'].unique()
plotConfirmed( countries ) 


