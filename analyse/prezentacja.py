import currencyNBP as nbp
import matplotlib.pyplot as plt
import pandas as pd
import trendsscraping as trends
import matplotlib.ticker as plticker

def wykresJednaWaluta( row, column,  notowania, nazwaWaluty, axes ):
    """Przygotowuje 1podwykres waluy, dla podanego przedziału w latach"""
    notowania.plot(ax=axes[row,column], y = 'mid', kind = 'line', title = nazwaWaluty, grid = True, fontsize = 6, figsize = ( 8, 8.66 ) )

def wykresCzteryWaluty( dataPoczatek, dataKoniec, waluty ):
    """Przygotowuje 4 wykresy walut, dla podanego przedziału w latach"""   

    fig, axes = plt.subplots(nrows=2, ncols=2)
    x = 0
    y = 0
    for waluta in waluty:
       notowania = nbp.notowaniaLata( 2019, 2020, waluta ) 
       wykresJednaWaluta( x%2, y%2,  notowania, waluta, axes )
       x+=1
       if x%2:
           y+=1
    plt.savefig('czteryWaluty', dpi=None, facecolor='w', edgecolor='w',\
        orientation='portrait', papertype='a4', format=None,\
        transparent=False, bbox_inches=None, pad_inches=0.1,\
        frameon=None, metadata=None)

def wykresCzteryNaJeden( dataPoczatek, dataKoniec, waluty ):
    """Przygotowuje wykres czterech walut, dla podanego przedziału w latach"""
    fig, ax = plt.subplots()
    loc = plticker.MultipleLocator(base=60)
    ax.xaxis.set_major_locator(loc)
    ax.grid()
    for waluta in waluty:
        notowanie = nbp.notowaniaLata( dataPoczatek, dataKoniec, waluta )
        ax.plot( notowanie.index, notowanie['mid'], label ='linear')
    
    fig.savefig('czteryWalutyJedenWykres', dpi=None, facecolor='w', edgecolor='w',\
        orientation='portrait', papertype='a4', format=None,\
        transparent=False, bbox_inches=None, pad_inches=0.1,\
        frameon=None, metadata=None)  
      



