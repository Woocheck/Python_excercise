import requests
import csv
from bs4 import BeautifulSoup as bs

url = requests.get("https://www.orlen.pl/PL/DlaBiznesu/HurtoweCenyPaliw/Strony/archiwum-cen.aspx?Fuel=Pb95&Year=2020")
soup = bs( url .content, 'html.parser')

filename = 'test.csv'

csv_writer = csv.writer( open( filename, 'w'))

heading = soup.find('table_responsive')
print(heading.text)