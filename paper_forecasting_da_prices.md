## Forecasting day ahead electricity spot prices: The impact of the EXAA to other European electricity markets

* Energy Exchange Austria (EXAA)
* The EXAA trades only on working days and not on weekends and Austrian public holidays. Therefore on a Friday of a common week there will be traded three days, Saturday, Sunday and Monday.
* The EXAA reveals their prices approximately at 10:20 pm, whereas offers to the EPEX can be submitted until 12:00 pm.
* cross border flow to Germany: Switzerland, Czech Republic, Denmark, France, Hungary, Italy, Netherlands, Poland, Slovenia and Sweden
* Besides the classical approach which uses historical data, we utilize the data of the EXAA for the next
day that is available at 10:25 (CET), prior to the submission time point of the other electricity markets.
* EXAA has hourly data
* AR(p) as basic model -> Especially the AR(p) modeling approach is considered as fundamental for an econometric analysis of electricity prices.
* Diebold-Mariano (DM) test to compare the forecasting perfor- mance
* models:
    1. persitent (naive): predict price based on the price 168h ago (1 week)
    2. univariate AR(p) -> pmax = 1400 (take model with minimal AIC)
    3. persistent EXAA based: predict price based on EXAA price (because it is published earlier)
    4. 2d AR(p): price + EXAA price (2 features)
    5. modified 2d AR(p): includes the EXAA forecasted values as well
    6. Difference based AR(p): AR(p) based on the difference between target price and EXAA price -> pmax = 1400
* results: 
    * Interestingly, the na ̈ıve EXAA model, which simply uses the price of the EXAA as predictor, turned out to be the best model for the EPEX Germany
    * It turned out that including the EXAA information in standard and robust time series approaches increased the performance of those models for every examined market.