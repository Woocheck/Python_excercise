import currencyNBP as nbp
import orlen
import trendsscraping as trends
import prezentacja as pr

waluty = [ "usd", "gbp", "eur", "jpy" ]
print(orlen.hurtoweCenyPaliw(2019,2020,'Pb95') )
pr.wykresCzteryWaluty( 2019, 2020, waluty)
print( trends.trendsInterestOverTime('2019-01-01', '2020-05-15',["Wuhan", "covid", "covid-19", "Italy" , "China"]))