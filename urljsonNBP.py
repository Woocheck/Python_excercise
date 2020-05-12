
import json
import requests
from urllib.parse import urlencode
import pandas as pd



host = "http://api.nbp.pl/api/exchangerates/rates/a"

currency = [ "usd", "gbp", "eur", "jpy" ]

year = 2019
beginDate = "-01-01"
endDate = "-12-31"
url = host +"/"+ currency[1] +"/"+ str(year) + beginDate +"/"+ str(year) + endDate +"/?"

data = json.loads(requests.get(url).text)

df = pd.DataFrame.from_dict(data, orient='columns')
print(df.head())