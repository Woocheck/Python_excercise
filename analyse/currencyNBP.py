
import json
import requests
from urllib.parse import urlencode
import pandas as pd


def notowaniaRok( year, currency ):
    """Return currency quotationsfor selected year, and list of currencyes """
    
    host = "http://api.nbp.pl/api/exchangerates/rates/a"
    url = host +"/"+ currency +"/"+ str(year) + "-01-01/"+ str(year) + "-12-31/"

    data = json.loads(requests.get(url).text)
    df = pd.DataFrame.from_dict(data, orient='columns')
    
    return df
    