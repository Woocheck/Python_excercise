import requests
from bs4 import BeautifulSoup as bs
import re
from urllib.parse import urlencode
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as plticker

def cenyPaliwa( dataPoczatek, dataKoniec, rodzajPaliwa):
    """Przygotowuje dane hurtowych cen paliwa dla wybranego przedziału czasowego"""
    listaWynik = []
    slownikGotoweDane = {}
    
    #pobieranie daneych tekstowych ze stony
    for rok in range(0,dataKoniec-dataPoczatek+1):
        zwracaneDane = { 'Fuel' : rodzajPaliwa, 'Year' : dataPoczatek+rok }
        orlenUrl = "https://www.orlen.pl/PL/DlaBiznesu/HurtoweCenyPaliw/Strony/archiwum-cen.aspx?"
        urlReqest = requests.get(orlenUrl + urlencode(zwracaneDane) )
        soup = bs( urlReqest .content, 'html.parser')
    #wybieranie danych tabelarycznych przy  pomocy wyrażeń regularnych
        surowyRekord = re.compile( r'\d\d-\d\d-\d\d\d\d\d\s\d\d\d') 
        suroweDane = surowyRekord.findall( soup.get_text() )
        suroweDane = [el.replace('\xa0','') for el in suroweDane]
        listaWynik.extend( suroweDane )
    #dane tekstowe przeniesione do słownika
    for notowanie in listaWynik:
        data = notowanie[0:10]
        kwota = notowanie[10:]
        slownikGotoweDane[data] = int(kwota)
    #słownik zamieniony na DataFrame
    cenyPaliw = pd.DataFrame.from_dict(slownikGotoweDane, orient='index')
    cenyPaliw.index = pd.to_datetime( cenyPaliw.index, dayfirst=True)

    return cenyPaliw

def hurtoweCenyPaliw( data_poczatek, data_koniec, rodzajPaliwa):
    """Przygotowuje dane cen paliw dla listy rodzajów paliwa w okreslonym przedziale lat"""
    hurtoweCenyPaliw = pd.DataFrame( columns = rodzajPaliwa )
    for paliwo in rodzajPaliwa:
        cenaPaliwa = cenyPaliwa( int(data_poczatek[:4]), int(data_koniec[:4]), paliwo )
        hurtoweCenyPaliw[ paliwo ] = cenaPaliwa[ 0 ]
    return hurtoweCenyPaliw
        

def wykresCenyPaliw( hurtowe_ceny_paliw ):
    """Funkcja przygotowuje wykres hurtowych cen paliw koncernu Orlen"""
    hurtowe_ceny_paliw.plot( title = ('Hurtowe ceny paliw'),\
                      grid = True,\
                      fontsize = 8,\
                      figsize = ( 8, 8 ))
    plt.legend()
    plt.xlabel("Data")
    plt.savefig('paliwoCeny', dpi=None, facecolor='w', edgecolor='w',\
                orientation='portrait', papertype='a4', format=None,\
                transparent=False, bbox_inches=None, pad_inches=0.1,\
                metadata=None) 
    

