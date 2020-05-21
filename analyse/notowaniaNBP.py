
import json
import requests
from urllib.parse import urlencode
import pandas as pd
import datetime
import matplotlib.pyplot as plt
from datetime import timedelta
import matplotlib.ticker as plticker

def notowaniaRok( rok, waluta ):
    """Zwraca notowania waluty dla danego roku"""
    
    host = "http://api.nbp.pl/api/exchangerates/rates/a"
    poczatek = str(rok) + "-01-01"
    if rok == datetime.date.today().year:
        koniec = (datetime.date.today() - timedelta(1)).strftime('%Y-%m-%d')
    else:
        koniec = str(rok) + "-12-31"
    url = host +"/"+ waluta +"/"+ poczatek +"/"+ koniec +"/"
    data = json.loads(requests.get(url).text)
    df = pd.DataFrame.from_dict(data, orient='columns')
    return df

def notowaniaLata( poczatek, koniec, waluta):
    """Zwraca notowania waluty dla przedziału podango w latach"""
    daneNBP = pd.DataFrame(columns = ['effectiveDate','mid'])
    for rok in range( 0,(koniec - poczatek+1)):
        daneRok = notowaniaRok( poczatek+rok, waluta ) 
        daneNBP = daneNBP.append( pd.concat([daneRok.drop('rates', axis=1), \
                                  pd.DataFrame(daneRok['rates'].tolist())], \
                                  axis=1)[['effectiveDate','mid']] ) 
    daneNBP = daneNBP.set_index('effectiveDate')  
    return daneNBP

def kursyWalutNBP( data_poczatek, data_koniec, lista_walut ):
    """Zwraca tabelę z kursami walut dla wybranych lat"""
    kursy_walut = pd.DataFrame(columns = lista_walut  )
    for waluta in lista_walut:
        notowania_NBP = notowaniaLata(int(data_poczatek[:4]), int(data_koniec[:4]), waluta )
        kursy_walut[ waluta ] = notowania_NBP[ 'mid' ]
    return kursy_walut

def wykresJednaWaluta( row, column,  notowania, nazwaWaluty, axes ):
    """Przygotowuje 1podwykres waluy, dla podanego przedziału w latach"""
    notowania.plot(ax=axes[row,column], y = 'mid', kind = 'line', title = nazwaWaluty, grid = True, fontsize = 6, figsize = ( 8, 8.66 ) )

def wykresCzteryWaluty( dataPoczatek, dataKoniec, waluty ):
    """Przygotowuje 4 wykresy walut, dla podanego przedziału w latach"""   

    fig, axes = plt.subplots(nrows=2, ncols=2)
    x = 0
    y = 0
    for waluta in waluty:
       notowania = notowaniaLata( 2019, 2020, waluta ) 
       wykresJednaWaluta( x%2, y%2,  notowania, waluta, axes )
       x+=1
       if x%2:
           y+=1
    plt.savefig('czteryWaluty', dpi=None, facecolor='w', edgecolor='w',\
        orientation='portrait', papertype='a4', format=None,\
        transparent=False, bbox_inches=None, pad_inches=0.1,\
        frameon=None, metadata=None)

def wykresWalutyNaJeden( dataPoczatek, dataKoniec, waluty ):
    """Przygotowuje wykres listy walut, dla podanego przedziału w latach"""
    fig, ax = plt.subplots()
    loc = plticker.MultipleLocator(base=60)
    ax.xaxis.set_major_locator(loc)
    ax.grid()
    for waluta in waluty:
        notowanie = notowaniaLata( int(dataPoczatek[:4]), int(dataKoniec[:4]), waluta )
        ax.plot( notowanie.index, notowanie['mid'], label ='linear')

    fig.savefig('walutyJedenWykres', dpi=None, facecolor='w', edgecolor='w',\
                orientation='portrait', papertype='a4', format=None,\
                transparent=False, bbox_inches=None, pad_inches=0.1,\
                metadata=None)