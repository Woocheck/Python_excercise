import pandas as pd
import matplotlib.pyplot as plt

def wykresZestawienie( daneNBP, daneTrends ):
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