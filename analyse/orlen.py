import requests
import csv
from bs4 import BeautifulSoup as bs
import re
from urllib.parse import urlencode

def hurtoweCenyRopy( dataPoczatek, dataKoniec, rodzajPaliwa):
    listaWynik = []
    slownikGotoweDane = {}
    for rok in range(0,dataKoniec-dataPoczatek+1):
        zwracaneDane = { 'Fuel' : rodzajPaliwa, 'Year' : dataPoczatek+rok }
        orlenUrl = "https://www.orlen.pl/PL/DlaBiznesu/HurtoweCenyPaliw/Strony/archiwum-cen.aspx?"
        urlReqest = requests.get(orlenUrl + urlencode(zwracaneDane) )
        soup = bs( urlReqest .content, 'html.parser')

        surowyRekord = re.compile( r'\d\d-\d\d-\d\d\d\d\d\s\d\d\d') 
        suroweDane = surowyRekord.findall( soup.get_text() )
        suroweDane = [el.replace('\xa0','') for el in suroweDane]
        listaWynik.extend( suroweDane )
    for notowanie in listaWynik:
        data = notowanie[0:10]
        kwota = notowanie[10:]
        slownikGotoweDane[data] = int(kwota)
    return slownikGotoweDane
    
    
print( hurtoweCenyRopy(2018,2020,'Pb95'))