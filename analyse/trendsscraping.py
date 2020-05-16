import pandas as pd                        
from pytrends.request import TrendReq
import matplotlib.pyplot as plt

def trendsInterestOverTime( dataPoczatek, dataKoniec, listaHasel):
    pytrends = TrendReq()
    przedzial = dataPoczatek+' '+dataKoniec
    print(przedzial)
    pytrends.build_payload(listaHasel, cat=0, timeframe= przedzial, geo='', gprop='')
    wynik = pytrends.interest_over_time()
    return wynik



listaHasel = ["Wuhan", "covid", "covid-19", "Italy" , "China"]
trendy = trendsInterestOverTime( '2018-01-01', '2020-05-15',listaHasel)
trendy.plot()
plt.show()