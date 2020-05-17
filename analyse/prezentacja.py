import currencyNBP as nbp
import matplotlib.pyplot as plt
import pandas as pd

def plotCases( row, column,  notowania, nazwaWaluty ):
    notowania.plot(ax=axes[row,column], x = 'effectiveDate', y = 'mid', kind = 'line', title = nazwaWaluty, grid = True, fontsize = 6, figsize = ( 8, 8.66 ) )

waluty = [ "usd", "gbp", "eur", "jpy" ]

fig, axes = plt.subplots(nrows=2, ncols=2)
x = 0
y = 0
for waluta in waluty:
   notowania = nbp.notowaniaLata( 2019, 2020, waluta ) 
   plotCases( x%2, y%2,  notowania, waluta )
   x+=1
   if x%2:
       y+=1

plt.show()