import pandas as pd
from pytrends.request import TrendReq
import csv
import pandas

pytrend = TrendReq()

pytrend.build_payload(kw_list=['covid-19'])



# Interest by Region
interest_by_region_df = pytrend.interest_by_region()
print(interest_by_region_df.head(20))

# Related Queries, returns a dictionary of dataframes
related_queries_dict = pytrend.related_queries()
print(related_queries_dict)

# Get Google Hot Trends data
trending_searches_df = pytrend.trending_searches()
print(trending_searches_df.head(20))

# Get Google Hot Trends data
today_searches_df = pytrend.today_searches()
print(today_searches_df.head(20))

# Get Google Top Charts
top_charts_df = pytrend.top_charts(date = 2020, hl='en-US', tz=300, geo='PL')
print(top_charts_df.head(20))

# Get Google Keyword Suggestions
suggestions_dict = pytrend.suggestions(keyword='poland')
print(suggestions_dict)