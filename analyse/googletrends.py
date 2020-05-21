import pandas as pd                        
from pytrends.request import TrendReq
import matplotlib.pyplot as plt

def trendsDlaPzedzialuCzasu( dataPoczatek, dataKoniec, listaHasel):
    """Funkcja pobiera dan z google trends dla wybranego rzedziału czasowego."""
    pytrends = TrendReq()
    #Formatowanie parametru 'timefrem z dat dla wybranego przedziału
    przedzial = dataPoczatek+' '+dataKoniec
    pytrends.build_payload(listaHasel, cat=0, timeframe= przedzial, geo='', gprop='')
    wynik = pytrends.interest_over_time()
    #Usuwanie zbędnej kolumny przekazywanej w wynikach zapytania
    del wynik['isPartial']
    return wynik

def obliczSrednia( dane ):
    """Funkcja oblicza średnią i umieszcza wynik w osobnej kolumnie."""
    dane['Średnia'] = dane.mean(axis=1)
    return dane

def korelacja( dane ):
    """Funkcja zwraca tabelę korelacji."""

    korelacja = dane.corr()
    pd.set_option("display.precision", 4)
    
    print( korelacja )
    korelacja.to_html('table.html')

def wykresDlaListy( dataPoczatek, dataKoniec, listaHasel ):
    daneTrends = trendsDlaPzedzialuCzasu( dataPoczatek, dataKoniec, listaHasel)
    daneTrends.plot()
    plt.show()

def wykresSrednia( dane ):
    daneSrednia = obliczSrednia( dane )
    daneSrednia['Średnia'].plot()
    plt.show()

    

