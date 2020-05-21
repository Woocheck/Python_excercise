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
    Dane['Średnia'] = wynik.mean(axis=1)


