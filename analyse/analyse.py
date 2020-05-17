import currencyNBP as nbp
import orlen
import trendsscraping as trends


print(orlen.hurtoweCenyPaliw(2019,2020,'Pb95') )
print(nbp.notowaniaLata( 2019, 2020, 'eur') )
print( trends.trendsInterestOverTime('2019-01-01', '2020-05-15',["Wuhan", "covid", "covid-19", "Italy" , "China"]))