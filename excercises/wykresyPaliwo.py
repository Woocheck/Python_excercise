import orlen 
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.ticker as plticker

def wykresCenyPaliw( dataPoczatek, dataKoniec, rodzajPaliwa):
    danePaliwo = orlen.hurtoweCenyPaliw(2019,2020,'Pb95')
    danePaliwo.plot()
    plt.show()

wykresCenyPaliw(2019,2020,'Pb95')