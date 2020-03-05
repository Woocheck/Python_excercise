import pandas as pd

pasengersData = pd.read_csv('titanic.csv')

print( pasengersData.head() )

thirdClassPassengers = pasengersData[ (pasengersData['Pclass'] == 3) & (pasengersData['Embarked'] == 'Q') ]

print( thirdClassPassengers.head() )

thirdClassPassengers.to_csv( 'titanicthirdClass.csv', ',')

pasengersData['Name'].str.upper()

print( thirdClassPassengers.head() )