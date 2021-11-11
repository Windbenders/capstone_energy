## ES Crossboarder Flows

General information:

* observations: 142816
* features: 4 [power_mw, from_country, to_country, type]
    * power_mw: power in MW
    * from_country: country providing energy
    * to_country: country receiving energy
    * type: crossboarder_flow
* start date: 2016-12-31 23:00:00
* end date: 2019-09-20 02:00:00
* time steps: 1 hour

## ES Forecast

* observations: 36876431
* features: 5 [power_mw, carrier, type, area, version_utc]
    * power_mw: power in MW
    * carrier: ['Gesamt', 'Solar', 'Wind Offshore', 'Wind Onshore']
    * type: ['Load Forecast', 'Renewables Forecast']
    * area: ['50Hertz', 'DE', 'DK', 'DK1', 'TTG']
    * version_utc: ?
* start date: 2016-12-31 23:00:00
* end date: 2021-07-14 21:45:00
* time steps: 15 min

## Imbalance DE

* observations: 257010
* features: 2 (unknown meaning, probably power in MW)
    * 1st column:
    * 2nd column: 
* start date: 2013-12-31 23:00:00
* end date: 2021-05-22 22:00:0
* time steps: 15 min

## epex da de json

* observations: 144911
* features: 3 [sechs_h_regelung, epex_da_de_eur_mwh, epex_da_de_mwh]
    * sechs_h_regelung: boolean, 6-hour rule a provision to reduce subsidies when electricity prices are negative
    * epex_da_de_eur_mwh: price in EUR per MWh
    * epex_da_de_mwh: NULL for all entries
* start date: 2004-12-31 23:00:00
* end date: 2021-07-13 21:00:00
* time steps: 1 hour