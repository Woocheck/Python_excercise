import trendsscraping as trends
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.ticker as plticker


def wykresDlaListy( dataPoczatek, dataKoniec, listaHasel ):
    daneTrends = trends.trendsDlaPzedzialuCzasu( dataPoczatek, dataKoniec, listaHasel)
    daneTrends.plot()
    plt.show()

def wykresSrednia( dane ):
    daneSrednia = trends.obliczSrednia( dane )
    daneSrednia['Średnia'].plot()
    plt.show()


