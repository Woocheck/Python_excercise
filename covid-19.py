import pandas as pd
import matplotlib.pyplot as plt

def diagram( x, y ):
    
    plt.xlim( len(x) ,  len(y) )
    plt.plot( x, y,  label='Germany')
    plt.title( ' Confirmed ')
    plt.legend()
    plt.grid(True)
    plt.show()

confirmed = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv')

#print( confirmed.head() )
x = confirmed.columns[ 4:]
y = confirmed[ confirmed['Country/Region'] == 'Germany' ]
print( x.shape )
print( y[4:].shape )
diagram( x, y )


