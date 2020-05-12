import pandas as pd                        
from pytrends.request import TrendReq
import matplotlib.pyplot as plt


pytrends = TrendReq()

kw_list = ["Wuhan"]
pytrends.build_payload(kw_list, cat=0, timeframe='today 5-y', geo='', gprop='')

df = pytrends.get_historical_interest(kw_list, year_start=2019, month_start=8, day_start=1, hour_start=0, year_end=2020, month_end=5, day_end=10, hour_end=0, cat=0, geo='', gprop='', sleep=0)

df.plot()

plt.show()
