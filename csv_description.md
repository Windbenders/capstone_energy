## __ES Crossboarder Flows__

* observations: 142816
* features: 4 [power_mw, from_country, to_country, type]
    * power_mw: power in MW
    * from_country: country providing energy
    * to_country: country receiving energy
    * type: crossboarder_flow
* start date: 2016-12-31 23:00:00
* end date: 2019-09-20 02:00:00
* time steps: 1 hour

## __ES Forecast__

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

## __Imbalance DE__

* observations: 257010
* features: 2 (unknown meaning, probably power in MW)
    * 1st column:
    * 2nd column: 
* start date: 2013-12-31 23:00:00
* end date: 2021-05-22 22:00:0
* time steps: 15 min

## __epex da de (json file)__

* observations: 144911
* features: 3 [sechs_h_regelung, epex_da_de_eur_mwh, epex_da_de_mwh]
    * sechs_h_regelung: boolean, 6-hour rule a provision to reduce subsidies when electricity prices are negative
    * epex_da_de_eur_mwh: price in EUR per MWh
    * epex_da_de_mwh: NULL for all entries
* start date: 2004-12-31 23:00:00
* end date: 2021-07-13 21:00:00
* time steps: 1 hour

 
## __'power_act_.csv'__

* In total we have 18 columns and 64328 rows 
* Columns names : 
['dt_start_utc', 'power_act_21', 'power_act_24', 'power_act_47' .....]
* date ranges from '2019-06-30' to  '2021-04-30'
* Date seems to be recorded for every 15 minutes
* All the columns contains missing values only for 'power_act_21' its 1.5% whereas >20% for other features

## __'power_fc_.csv'__

* In total we have 23 columns and 66020 rows 
* Columns names : 
['dt_start_utc', 'power_act_21', 'power_act_24', 'power_act_47' .....]
* date ranges from ''2019-06-13 07:00'' to  ''2021-04-30 23:45''
* Date seems to be recorded for every 15 minutes
* no null values for 'power_act_21'  whereas for other features >17% null values

## __'regelleistung_aggr_results.csv'__

* In total we have 17 columns and 16068 rows 
* Columns names : 
['date_start', 'date_end', 'product', 'reserve_type', 'total_min_capacity_price_eur_mw',#   
'total_average_capacity_price_eur_mw', 'total_marginal_capacity_price_eur_mw','total_min_energy_price_eur_mwh', 'total_average_energy_price_eur_mwh', 'total_marginal_energy_price_eur_mwh', 'germany_min_capacity_price_eur_mw',
'germany_average_capacity_price_eur_mw', 'germany_marginal_capacity_price_eur_mw','germany_min_energy_price_eur_mwh',
'germany_average_energy_price_eur_mwh', 'germany_marginal_energy_price_eur_mwh', 'germany_import_export_mw']
* 2 unique reserve type ['MRL', 'SRL']
* 12 unique product type ['NEG_00_04', 'NEG_04_08', 'NEG_08_12', 'NEG_12_16', 'NEG_16_20','NEG_20_24', 'POS_00_04', 'POS_04_08', 'POS_08_12', 'POS_12_16', 'POS_16_20', 'POS_20_24']
* date ranges from '2019-01-01' to  '2021-03-19'
* Date seems to be recorded for every hours (24 values for each days)
* 240 missing values each in 6 columns: ['total_min_energy_price_eur_mwh', 'total_average_energy_price_eur_mwh', 'total_marginal_energy_price_eur_mwh', 'germany_min_energy_price_eur_mwh', 'germany_average_energy_price_eur_mwh', 'germany_marginal_energy_price_eur_mwh'] 

## __'regelleistung_demand.csv'__

* In total we have 6 columns and 16188 rows 
* Columns names : ['date_start', 'date_end', 'product', 'total_demand_mw',
    'germany_block_demand_mw', 'reserve_type']
* 2 unique reserve type ['MRL', 'SRL']
* 12 unique product type ['NEG_00_04', 'NEG_04_08', 'NEG_08_12', 'NEG_12_16', 'NEG_16_20','NEG_20_24', 'POS_00_04', 'POS_04_08', 'POS_08_12', 'POS_12_16', 'POS_16_20', 'POS_20_24']
* date ranges from '2019-01-01' to  '2021-03-18'
* Date seems to be recorded for every hours (24 values for each days)
* no missing values

## __'onlinehochrechnung_solar_mw.csv'__

* In total we have 6 columns and 83,519 rows
* Columns names: ['dt_start_utc', 'fiftyhertz', 'tennet', 'amprion', 'transnetbw', 'nrv']
* data ranges from '2011-12-31 23:00:00' to '2021-07-11 21:00:00'
* Data is recorded for every 60 minutes
* no missing values

## __'onlinehochrechnung_windonshore_mw.csv'__

* In total we have 6 columns and 83,279 rows
* Columns names: ['dt_start_utc', 'fiftyhertz', 'tennet', 'amprion', 'transnetbw', 'nrv']
* data ranges from '2011-12-31 23:00:00' to '2021-07-01 21:00:00'
* Data is recorded for every 60 minutes
* no missing values

## __'onlinehochrechnung_windoffshore_mw.csv'__

* In total we have 6 columns and 74,735 rows
* Columns names: ['dt_start_utc', 'fiftyhertz', 'tennet', 'amprion', 'transnetbw', 'nrv']
* data ranges from '2012-12-31 23:00:00' to '2021-07-11 21:00:00'
* Data is recorded for every 60 minutes
* no missing values

## __'einspeisedaten_gen_wind_speed.csv'__

* In total we have 3 columns and 6,548,085 rows
* Columns names: ['dt_start_utc', 'voronoi_area_id', 'windspeed_ms']
* data ranges from '2018-12-31 23:00:00' to '2020-09-30 23:45:00'
* Data is recorded for every 15 minutes
* no missing values

---

## __Column name descriptions__

### __PRL = Prim??rRegelLeistung__
* Um die Normalfrequenz von 50 Hertz im bundesdeutschen Stromnetz jederzeit halten zu k??nnen, ben??tigen die vier deutschen ??bertragungsnetzbetreiber ein Werkzeug, das unvorhergesehene Schwankungen in Sekundenschnelle ausgleichen kann. 
* Dieses Werkzeug ist die Prim??rreserve (auch: ???Prim??rregelleistung", abgek??rzt PRL) oder vom Verbund der zentraleurop??ischen ??bertragungsnetzbetreiber ENTSO-E (???European Network of Transmission System Operators for Electricity") bezeichnete Frequency Containment Reserve (FCR), die innerhalb von 30 Sekunden verf??gbar sein muss, um einen Stromausfall verhindern zu k??nnen. 
* Somit ist die Prim??rreserve die erste zu aktivierende Regelenergieart und die unmittelbare Ma??nahme auf eine Abweichung der Netzfrequenz in unzul??ssigem Betriebsbereich.
* Da durch die Prim??rregelleistung vor allem kurzfristige Last??nderungen abgefedert werden sollen, muss die gesamte Angebotsleistung innerhalb von maximal 30 Sekunden vollst??ndig erbracht werden und f??r mindestens 15 Minuten durchgehend zur Verf??gung stehen.
### __SRL = Sekund??rRegelLeistung__
* Auch die Sekund??rregelung hat die Aufgabe, das Gleichgewicht zwischen physikalischem Stromangebot und -nachfrage nach dem Auftreten einer Differenz wiederherzustellen. 
* Im Gegensatz zur Prim??rregelung wird hier nur die Situation in der jeweiligen Regelzone inklusive des Stromaustausches mit anderen Regelzonen betrachtet. Daf??r werden die geplanten mit den tats??chlichen Leistungsfl??ssen zu anderen Regelzonen verglichen und ausgeregelt. Es muss sichergestellt sein, dass die Sekund??r- und Prim??rregelung immer in die gleiche Richtung arbeiten, was durch eine ??berwachung der Netzfrequenz sichergestellt wird. 
* Prim??r- und Sekund??rregelung k??nnen zeitgleich starten, der sekund??re Regelvorgang sollte entsprechend den Vorgaben des Netzregelverbundes nach sp??testens 15 Minuten den prim??ren Regelvorgang abgel??st haben, so dass die Prim??rregelung wieder zur Verf??gung steht.
* Die H??he der sekund??r zur Verf??gung gestellten Leistung h??ngt zum einen von der Netzkennzahl und der Frequenzabweichung ab, zum anderen von der Differenz aus den tats??chlichen Austauschleistungen zu Nachbarnetzen und den als Fahrplan deklarierten Austauschleistungen. 
* Der Abruf der Sekund??rregelleistung erfolgt automatisiert, dazu sind die entsprechenden Erzeugungseinheiten leittechnisch mit dem ??bertragungsnetzbetreiber verbunden. Erzeugereinheiten, die Sekund??rregelleistung bereitstellen, m??ssen dabei besondere Anforderungen erf??llen. 
* Die gesamte Regelleistung muss innerhalb von h??chstens 5 Minuten erbracht werden k??nnen, die Last??nderungsgeschwindigkeit muss dabei mindestens 2 % der Nennleistung pro Minute betragen. Zum Einsatz kommen dabei zum Beispiel Pumpspeicherkraftwerke oder auch konventionelle GuD- oder Steinkohlekraftwerke.

### __MRL = MinutenReserveLeistung (Terti??rregelung)__
* Auch bei der Terti??rregelung (Minutenreserve) wird zwischen negativer und positiver Regelenergie unterschieden, sie dient prim??r der wirtschaftlichen Optimierung. Fr??her wurde die Minutenreserve vom ??bertragungsnetzbetreiber beim Lieferanten telefonisch angefordert.

* Seit 3. Juli 2012 wird die Minutenreserve automatisch vom Merit-Order-List-Server (MOLS) abgerufen.

* Die vorgehaltene Minutenreserveleistung muss innerhalb von 15 Minuten vollst??ndig erbracht werden k??nnen, zum Einsatz kommen dabei konventionelle Kraftwerke oder andere Erzeugereinheiten, sowie regelbare Lasten.

* Als regelbare Lasten werden zum Beispiel Lichtbogen??fen in Stahlwerken oder Nachtspeicherheizungen verwendet.

* F??r die negative Minutenreserve stehen zwei M??glichkeiten zur Verf??gung:
    * Die Aktivierung zus??tzlicher Lasten im Netz in Form von Pumpspeicherkraftwerken.
    * Das teilweise oder komplette Herunterfahren von Kraftwerken. Neben der Drosselung von Gro??kraftwerken kann negative Regelleistung auch durch kollektives Abschalten von Blockheizkraftwerken (BHKW-Anlagen) in Form eines virtuellen Kraftwerks bereitgestellt werden. Dabei sind solche BHKW-Anlagen besonders geeignet, deren W??rmelieferung nicht kontinuierlich gew??hrleistet sein muss. Jedoch darf deren eingespeister Strom nicht nach EEG verg??tet werden, denn eine Parallelvermarktung steht derzeit dem EEG entgegen.
    * Auch durch Windkraft kann mittlerweile negative Minutenreserve bereitgestellt werden. Daf??r werden Windkraftanlagen in einem virtuellen Kraftwerk mithilfe von Fernsteuerung und auf Basis meteorologischer Daten, den Erzeugungsleistungen der Anlagen und der jeweiligen Signale der Netzbetreiber dem Bedarf entsprechend heruntergeregelt.


### __RZ = Regelzone__
Als "Regelzone" bezeichnet man einen geographisch festgelegten Verbund von Hoch- bzw. H??chstspannungsnetzen, deren Stabilit??t vom f??r sie zust??ndigen ??bertragungsnetzbetreiber (??NB) organisiert wird.

---

## __Transmission system operators__
### __Amprion__
* one of four transmission system operators in Germany
* extra-high-voltage network is 11,000 km long and transports electricity across an area that extends from Lower Saxony to the Alps.
* Around a third of Germany???s economic output is generated there.
* Also performs overarching operations for integrated grid systems in Germany and Europe
* 2 offshore wind farms: DOLWIN4 and BORWIN4 - operation start 2028
* https://www.amprion.net/
* Market Platform: Grid Losses, Reserve Power Plants, Control Energy, Interruptible Loads

### __TenneT__
* one of four transmission system operators in Germany and the Netherlands
* 27,000 high voltage pylons
* 24,000 km high-voltage network
* 99.9999% grid availability
* Onshore and Offshore projects: 14 total connected offshore wind farms
* 16 interconnections
* 42,000,000 end users
* https://www.tennet.eu/#&panel1-1

### __Transnet BW__
* one of four transmission system operators in Germany: Baden-W??rttemberg but ensure that electricity is supplied to the region, Germany and throughout Europe
* former part of EnBW, spun off to separate company due to the European Commission's requirements for the liberalisation of the energy market
* power grid lines of 3,200 km
* 11,000,000 end users
* cooperation with Amprion for the Ultranet grid expansion project
* cooperation with TenneT: planning and implementing SuedLink wind power line (700 km, largest infrastructure project, north-south connection)
* https://www.transnetbw.de/de
* Link to infeed: https://www.transnetbw.com/en/transparency/market-data/key-figures

### __50Hertz__
* 50Hertz Transmission is one of four transmission system operators in Northern and Eastern Germany
* power grid lines of 10,380 km
* 18,000,000 end users
* 50Hertz is a forerunner in the field of secure integration of renewable energy: in our grid area, more than 60 percent of the electricity consumed is already generated from renewable sources ??? until 2032 we want to integrate 100 percent securely.
* 2 Offshore Wind parks: Ostwind 2 (GER), Arcadis Ost 1 (Belgian Wind Park Operator Parkwind)
* Connect Arcadis Ost 1 and Baltic Eagle (both Baltic Sea)- installation of third cable system planned for 2022

### __NRV NetzRegelVerbund__
* Grid Control Cooperation: innovative network control concept, by means of which the four German transmission system operators (TSOs) optimise their control energy use and the control reserve provision technically and economically through an intelligent communication between the load-frequency controllers of the TSOs
* TSOs: 50Hertz, Amprion, TenneT, Transnet BW
* https://www.regelleistung.net/apps/datacenter/activated-values/?cooperation=NRV&qualities=OPERATIONAL&qualities=ASSURED&seriesGroups=HIJQag%2BgIgohCCMAKEkBUCMBWAskA