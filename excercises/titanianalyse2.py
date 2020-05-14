import pandas as pd
import pylab as plb
import matplotlib.pyplot as plt

titanicPassengers = pd.read_csv('C:/Users/wooch/Documents/GitHub/Python_excercise/excercises/titanic.csv')

print( titanicPassengers )

titanicPassengers['Age'].hist()
titanicPassengers['Pclass']

pierwszaKlasa = titanicPassengers[ (titanicPassengers['Pclass'] == 3 ) & (titanicPassengers['Survived'] == 1 ) ]
pierwszaKlasa['Age'].hist()
plt.grid(True)
plt.show()