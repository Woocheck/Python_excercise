import pandas as pd

dataTitanic = pd.read_csv('C:/Users/wooch/Desktop/zadania/titanic.csv')

print( dataTitanic.shape)
print(dataTitanic.columns)
dataTitanic.drop( ['Surname','Name'], axis=1, inplace=True)

dataTitanic.drop([0,1,2,3,4], axis=0, inplace=True)

print(dataTitanic.head())
