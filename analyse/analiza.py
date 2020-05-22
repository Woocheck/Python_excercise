import pandas as pd
import notowaniaNBP as nbp
import orlen
import googletrends as trends


#Przedział czasu rozpatrywany w analizie
data_poczatek = '2019-12-01'
data_koniec   = '2020-05-15'

### Pobieranie i porządkowanie Danych do analizy ###
#1. Google Trends
lista_hasel = [ "Wuhan", "covid", "covid-19", "Italy" , "China" ]
trends_dane = trends.trendsDlaPzedzialuCzasu( data_poczatek, data_koniec, lista_hasel )
srednia = trends.obliczSrednia( trends_dane )
korelacja = trends.korelacja( trends_dane )

#2. Kursy walut - dnae z NBP
lista_walut = [ "usd", "gbp", "eur", "chf" ]
kursy_walut = nbp.kursyWalutNBP( data_poczatek, data_koniec, lista_walut )

#3. Średnie ceny paliwa - Orlen
rodzaje_paliw = ["Pb95", "Pb98", "ONEkodiesel", "ONEkoterm" ]
hurtowe_ceny_paliw = orlen.hurtoweCenyPaliw( data_poczatek, data_koniec, rodzaje_paliw )

#Prezentacja Danych
#1. Google Trends
trends.wykresDlaListy( trends_dane )
trends.wykresSrednia( srednia )
#2. Kursy walut - dnae z NBP
nbp.wykresCzteryWaluty( data_poczatek, data_koniec, lista_walut )
nbp.wykresyWalutRazem( kursy_walut )
#3. Średnie ceny paliwa - Orlen
orlen.wykresCenyPaliw( hurtowe_ceny_paliw )

#Zestawienie 