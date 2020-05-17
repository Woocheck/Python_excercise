
import json
import requests
from urllib.parse import urlencode
import pandas as pd
import datetime
from datetime import timedelta

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
