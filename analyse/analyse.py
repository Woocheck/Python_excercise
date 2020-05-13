import currencyNBP as nbp
import matplotlib.pyplot as plt
import pandas as pd

def plotCases( row, column,  data, diagramTitle ):
    data.plot(ax=axes[row,column], x =data['effectiveDate'], y = data['mid'], kind = 'line', title = diagramTitle, grid = True, fontsize = 6, figsize = ( 8, 8.66 ) )
currences = [ "usd", "gbp", "eur", "jpy" ]

fig, axes = plt.subplots(nrows=2, ncols=2)
x = 0
y = 0
for element in currences:
   df = nbp.currencyYear( 2019, "usd" )
   daneNBP = pd.concat([df.drop('rates', axis=1), pd.DataFrame(df['rates'].tolist())], axis=1)
   notowania = daneNBP[['effectiveDate','mid']]
   print(notowania)
   #plotCases( x, y,  notowania, element )
   x +=1
   if x>1:
       x=0
       y +=1
   if y>1:
       y=0


