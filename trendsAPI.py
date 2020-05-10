import pandas as pd #pandas 0.25
from pytrends.request import TrendReq
pytrend = TrendReq()

trending_searches_df = pytrend.trending_searches(pn='poland')
print(trending_searches_df.head(40))

today_searches = pytrend.today_searches(pn='US')
print(today_searches.head(40))