import currencyNBP as nbp
import matplotlib.pyplot as plt
import pandas as pd
import trendsscraping as trends

def wykresJednaWaluta( row, column,  notowania, nazwaWaluty, axes ):
    notowania.plot(ax=axes[row,column], y = 'mid', kind = 'line', title = nazwaWaluty, grid = True, fontsize = 6, figsize = ( 8, 8.66 ) )

def wykresCzteryWaluty( dataPoczatek, dataKoniec, waluty ):
    """Przygotowuje wykres czterech walut, dla podanego przedziału w latach"""   
    fig, axes = plt.subplots(nrows=2, ncols=2)
    x = 0
    y = 0
    for waluta in waluty:
       notowania = nbp.notowaniaLata( 2019, 2020, waluta ) 
       wykresJednaWaluta( x%2, y%2,  notowania, waluta, axes )
       x+=1
       if x%2:
           y+=1
    plt.show()


listaHasel = ["Wuhan", "covid", "covid-19", "Italy" , "China"]
trendy = trends.trendsInterestOverTime( '2019-01-01', '2020-05-15',listaHasel)
trendy.plot()

plt.show()