# Notes


## Kind of problem
* Regression

## Target
*


## Included features
1) base production
2) system load
3) solar and wind generation
4) seasonality
5) day-ahead price
6) balance volume contributions

### Most promising features
1) Net Imbalance Volume
2) LOLP (aggregated) (Which aggregation level and method?)
3) Month
4) Re-rated margins (aggregated) (Which aggregation level and method?) (What are margins?)

## ML-Algorithms
1) Gradient Boosting (GB)
2) Random Forest (RF) 
3) XGBoost

### Most promising algorithm
* XGBoost

## Regression metrics
1) Mean Absolute Error (MAE)
2) Coefficient of determination (R2 score) 
3) Mean Squared Error (MSE)

## Main findings
* High precision prediction close to impossible
* More promising approach

## Abbreviations:
* LOLP = Loss of Load Probability
* Re-rated margins
- "De-rated capacity margin represents a metric which could be used to measure electricity security of supply as well as to set a **reliability** standard. The **de-rated capacity margin** measures the **amount of excess supply above peak demand**. De-rating means that the supply is adjusted to take account of the availability of plant, specific to each type of generation technology. It reflects the proportion of an electricity source, which is likely to be technically available to generate at times of peak demand." \
(Source: https://www.emissions-euets.com/internal-electricity-market-glossary/449-de-rated-capacity-margin)
-  "In broad terms, therefore, the capacity margin is calculated from two variables: the 
**expected level of peak electricity demand** and the **expected level of available power generation** at the time of peak demand." \
(Source: https://www.raeng.org.uk/publications/reports/gb-electricity-capacity-margin)
- Formula:
$capacity\ margin\ =  \frac{total\ available\ capacity - peak\ demand}{peak\ demand} * 100
$                                  

- 

