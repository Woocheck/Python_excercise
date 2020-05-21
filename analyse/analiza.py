import pandas as pd
import notowaniaNBP as nbp
import orlen
import googletrends as trends


#Przedział czasu rozpatrywany w analizie
data_poczatek = '2019-12-01'
data_koniec   = '2020-05-15'

#Pobieranie Danych do analizy
#1. Google Trends
lista_hasel = [ "Wuhan", "covid", "covid-19", "Italy" , "China" ]
#TODO:Related Queries
trends_dane = trends.trendsDlaPzedzialuCzasu( data_poczatek, data_koniec, lista_hasel )

#2. Kursy walut - dnae z NBP
lista_walut = [ "usd", "gbp", "eur", "chf" ]
kursy_walut = pd.DataFrame(columns = lista_walut  )
kursy_walut = nbp.kursyWalutNBP( data_poczatek, data_koniec, lista_walut )
nbp.wykresWalutyNaJeden( data_poczatek, data_koniec, lista_walut )
#3. Średnie ceny paliwa - Orlen


