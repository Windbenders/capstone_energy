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

 
## 'power_act_.csv'

In total we have 18 columns and 64328 rows 

Columns names : 
['dt_start_utc', 'power_act_21', 'power_act_24', 'power_act_47' .....]


date ranges from '2019-06-30' to  '2021-04-30'

Date seems to be recorded for every 15 minutes

All the columns contains missing values only for 'power_act_21' its 1.5% whereas >20% for other features

## 'power_fc_.csv'

In total we have 23 columns and 66020 rows 

Columns names : 
['dt_start_utc', 'power_act_21', 'power_act_24', 'power_act_47' .....]


date ranges from ''2019-06-13 07:00'' to  ''2021-04-30 23:45''

Date seems to be recorded for every 15 minutes

no null values for 'power_act_21'  whereas for other features >17% null values

## 'regelleistung_aggr_results.csv'

In total we have 17 columns and 16068 rows 

Columns names : 
['date_start', 'date_end', 'product', 'reserve_type', 'total_min_capacity_price_eur_mw',#   
'total_average_capacity_price_eur_mw', 'total_marginal_capacity_price_eur_mw','total_min_energy_price_eur_mwh', 'total_average_energy_price_eur_mwh', 'total_marginal_energy_price_eur_mwh', 'germany_min_capacity_price_eur_mw',
'germany_average_capacity_price_eur_mw', 'germany_marginal_capacity_price_eur_mw','germany_min_energy_price_eur_mwh',
'germany_average_energy_price_eur_mwh', 'germany_marginal_energy_price_eur_mwh', 'germany_import_export_mw']

2 unique reserve type ['MRL', 'SRL']

12 unique product type ['NEG_00_04', 'NEG_04_08', 'NEG_08_12', 'NEG_12_16', 'NEG_16_20','NEG_20_24', 'POS_00_04', 'POS_04_08', 'POS_08_12', 'POS_12_16', 'POS_16_20', 'POS_20_24']

date ranges from '2019-01-01' to  '2021-03-19'

Date seems to be recorded for every hours (24 values for each days)

240 missing values each in 6 columns: ['total_min_energy_price_eur_mwh', 'total_average_energy_price_eur_mwh', 'total_marginal_energy_price_eur_mwh', 'germany_min_energy_price_eur_mwh', 'germany_average_energy_price_eur_mwh', 'germany_marginal_energy_price_eur_mwh'] 

## 'regelleistung_demand.csv'

In total we have 6 columns and 16188 rows 

Columns names : ['date_start', 'date_end', 'product', 'total_demand_mw',
    'germany_block_demand_mw', 'reserve_type']

2 unique reserve type ['MRL', 'SRL']

12 unique product type ['NEG_00_04', 'NEG_04_08', 'NEG_08_12', 'NEG_12_16', 'NEG_16_20','NEG_20_24', 'POS_00_04', 'POS_04_08', 'POS_08_12', 'POS_12_16', 'POS_16_20', 'POS_20_24']

date ranges from '2019-01-01' to  '2021-03-18'

Date seems to be recorded for every hours (24 values for each days)

no missing values

## 'onlinehochrechnung_solar_mw.csv'

In total we have 6 columns and 83,519 rows

Columns names: ['dt_start_utc', 'fiftyhertz', 'tennet', 'amprion', 'transnetbw', 'nrv']

data ranges from '2011-12-31 23:00:00' to '2021-07-11 21:00:00'

Data is recorded for every 60 minutes

no missing values

## 'onlinehochrechnung_windonshore_mw.csv'

In total we have 6 columns and 83,279 rows

Columns names: ['dt_start_utc', 'fiftyhertz', 'tennet', 'amprion', 'transnetbw', 'nrv']

data ranges from '2011-12-31 23:00:00' to '2021-07-01 21:00:00'

Data is recorded for every 60 minutes

no missing values

## 'onlinehochrechnung_windoffshore_mw.csv'

In total we have 6 columns and 74,735 rows

Columns names: ['dt_start_utc', 'fiftyhertz', 'tennet', 'amprion', 'transnetbw', 'nrv']

data ranges from '2012-12-31 23:00:00' to '2021-07-11 21:00:00'

Data is recorded for every 60 minutes

no missing values

## 'einspeisedaten_gen_wind_speed.csv'

In total we have 3 columns and 6,548,085 rows

Columns names: ['dt_start_utc', 'voronoi_area_id', 'windspeed_ms']

data ranges from '2018-12-31 23:00:00' to '2020-09-30 23:45:00'

Data is recorded for every 15 minutes

no missing values