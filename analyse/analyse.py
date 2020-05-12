import currencyNBP as nbp

currency = [ "usd", "gbp", "eur", "jpy" ]

data = nbp.currencyYear( 2019, "gbp" )

print( data.head() )
