import trendsscraping as trends
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.ticker as plticker


def wykresDlaListy( dataPoczatek, dataKoniec, listaHasel ):
    daneTrends = trends.trendsInterestOverTime( dataPoczatek, dataKoniec, listaHasel)
    daneTrends.plot()
    plt.show()


wykresDlaListy( '2019-09-01', '2020-05-15',["Wuhan", "covid", "covid-19", "Italy" , "China"])
