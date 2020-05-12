
import json
import requests
from urllib.parse import urlencode





host = "http://api.nbp.pl/api/exchangerates/rates/a"
currency = [ "usd", "gbp", "eur", "jpy" ]

year = 2019
beginDate = "-01-01"
endDate = "-12-31"
returnedFormat = { 'format' : 'json' }
url = host +"/"+ currency[1] +"/"+ str(year) + beginDate +"/"+ str(year) + endDate +"/?"

adres = url + urlencode(returnedFormat)

print( adres )

response = json.loads(requests.get(url).text)

print(json.dumps(response, indent=4, sort_keys=True))
