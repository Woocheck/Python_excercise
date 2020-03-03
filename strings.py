import pandas as pd

orders = pd.read_table('http://bit.ly/chiporders')

print( orders.head())

orders['item_name'].str.upper()
print( orders.head())

print( pd.__version__)
print( pd. show_versions())