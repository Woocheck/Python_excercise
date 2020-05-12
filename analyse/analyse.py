import currencyNBP as nbp

currences = [ "usd", "gbp", "eur", "jpy" ]

for element in currences:
    data = nbp.currencyYear( 2019, element )
    print( data.head() )
