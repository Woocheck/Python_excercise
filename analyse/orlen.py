import requests
import csv
from bs4 import BeautifulSoup as bs
import re

url = requests.get("https://www.orlen.pl/PL/DlaBiznesu/HurtoweCenyPaliw/Strony/archiwum-cen.aspx?Fuel=Pb95&Year=2020")
soup = bs( url .content, 'html.parser')

rawRecord = re.compile( r'\d\d-\d\d-\d{5} \d{3}') 
rawData = rawRecord.findall( soup.get_text() )

print( rawData )
