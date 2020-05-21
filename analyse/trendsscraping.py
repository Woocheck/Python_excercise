import pandas as pd                        
from pytrends.request import TrendReq
import matplotlib.pyplot as plt


def trendsDlaPzedzialuCzasu( dataPoczatek, dataKoniec, listaHasel):
    pytrends = TrendReq()
    przedzial = dataPoczatek+' '+dataKoniec
    pytrends.build_payload(listaHasel, cat=0, timeframe= przedzial, geo='', gprop='')
    wynik = pytrends.interest_over_time()
    del wynik['isPartial']
    return wynik
def obliczSrednia( dane ):
    dane['Średnia'] = dane.mean(axis=1)
    return dane

def korelacja( dane ):
    """Funkcja zwraca graficzną wersję tabeli korelacji."""

    korelacja = dane.corr()
    pd.set_option("display.precision", 4)
    print( korelacja )
    
    ax = plt.subplot(111, frame_on=False) 
    ax.axis("off")
    plt.table(cellText=korelacja.values ,colWidths = [0.5]*len(korelacja.columns),
          rowLabels=korelacja.index,
          colLabels=korelacja.columns,
          cellLoc = 'center', rowLoc = 'center',
          loc='top')
    plt.show()

