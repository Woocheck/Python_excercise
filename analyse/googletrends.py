import pandas as pd                        
from pytrends.request import TrendReq
import matplotlib.pyplot as plt
import matplotlib.ticker as plticker

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
    """Funkcja zwraca wyniki obliczeń korelacji."""
    korelacja = dane.corr()
    pd.set_option("display.precision", 4)
    return korelacja

def wykresDlaListy( dane_dla_listy_hasel ):
    fig, ax = plt.subplots()
    loc = plticker.MultipleLocator(base=60)
    ax.xaxis.set_major_locator(loc)
    ax.grid()
    
    for element in dane_dla_listy_hasel.columns:
        dane_dla_listy_hasel[element].plot( kind = 'line',\
                      title = ('Wyniki Google Trends dla listy haseł'),\
                      grid = True,\
                      fontsize = 11,\
                      figsize = ( 8, 8 ) )
    ax.legend()
    plt.xlabel("Data")
    fig.savefig('trendsDaneWykres', dpi=None, facecolor='w', edgecolor='w',\
                orientation='portrait', papertype='a4', format=None,\
                transparent=False, bbox_inches=None, pad_inches=0.1,\
                metadata=None)

def wykresSrednia( dane ):
    daneSrednia = obliczSrednia( dane )
    
    fig, ax = plt.subplots()
    loc = plticker.MultipleLocator(base=60)
    ax.xaxis.set_major_locator(loc)
    ax.grid()
    daneSrednia['Średnia'].plot( kind = 'line', title = ('Średnia z wynikow Gooogle Trends'), grid = True, fontsize = 11, figsize = ( 8, 8 ) )
    ax.legend()
    plt.xlabel("Data")
    fig.savefig('trendsSrednia', dpi=None, facecolor='w', edgecolor='w',\
                orientation='portrait', papertype='a4', format=None,\
                transparent=False, bbox_inches=None, pad_inches=0.1,\
                metadata=None)

    

