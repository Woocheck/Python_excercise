import requests
import lxml.html as lh
import pandas as pd

url='https://www.orlen.pl/PL/DlaBiznesu/HurtoweCenyPaliw/Strony/archiwum-cen.aspx?Fuel=Pb95&Year=2020'


page = requests.get(url)

