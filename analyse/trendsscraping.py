import pandas as pd                        
from pytrends.request import TrendReq
import matplotlib.pyplot as plt


pytrends = TrendReq()

kw_list = ["Wuhan", "covid", "covid-19", "Italy" ,"on"]
pytrends.build_payload(kw_list, cat=0, timeframe='2019-12-01 2020-05-12', geo='', gprop='')

dfpl = pytrends.interest_over_time()
dfpl.plot()

plt.show()
