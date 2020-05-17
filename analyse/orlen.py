import requests
from bs4 import BeautifulSoup as bs
import re
from urllib.parse import urlencode
import pandas as pd

def hurtoweCenyPaliw( dataPoczatek, dataKoniec, rodzajPaliwa):
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
    

