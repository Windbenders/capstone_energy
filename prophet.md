# __Prophet__

## __PROs__
* fast
* completely automated forecasts
* based on an additive model --> non-linear trends are fit with yearly, weekly, and daily seasonality, plus holiday effects
* released by Facebook's Core Data Science team
* forecasting procedure implemented in R and Python, so widely used languages
* algorithm provides useful statistics that help visualize the tuning process, e.g. trend, week trend, year trend and their max and min errors
* tunable
* accurate: MAE is smallest compared to XGBoost and ARIMA
* follows the sklearn model API
* input to Prophet is always a dataframe with two columns: 
    * ds (datastamp): ideally YYYY-MM-DD for a date or YYYY-MM-DD HH:MM:SS for a timestamp
    * y column must be numeric, and represents the measurement we wish to forecast

<br />

---
## __Additive and multiplicative models__

| __additive model__ | __multiplicative model__ |
| --- | --- |
| Data = _seasonal effect_ + _trend_ + _residuals_ | Data = _seasonal effect_ * _trend_ * _residuals_ | 

<br />

---

## __Install__

* in __Python__ install pystan with pip before using pip to install prophet
* pystan>=3.0 is currently not supported

```
pip install pystan==2.19.1.1

pip install prophet
```

* in __Anaconda__ 2 options, conda-forge the easiest

````
conda install gcc


#easiest way

conda install -c conda-forge prophet
````

---

## __Import and work with Prophet in Python__

```````
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import os

plt.style.use('fivethirtyeight')
print(os.listdir("../input"))

import statsmodels.api as sm
from fbprophet import Prophet
import xgboost as xgb

from sklearn.metrics import mean_absolute_error
````````

```````
def split_data(data, split_date):
    return data[data.index <= split_date].copy(), \
           data[data.index >  split_date].copy()

def limit(data, frm, to):
    return data[(data.index>=frm)&(data.index<to)]
`````````

```````
dataset_hourly = pd.read_csv('../data/data_hourly.csv', 
                            index_col=[0], parse_dates=[0])
dataset_hourly.sort_index(inplace=True)

t = dataset_hourly.column_name.copy()
t = t.drop(t.index[t.index.duplicated()])
freq_index = pd.date_range(start=t.index[0], end=t.index[-1], freq='H')
constructed = pd.Series(index=freq_index, name='column_name')
constructed.update(t)
constructed.interpolate(inplace=True)
train, test = split_data(constructed, 'DD-MM-YYYY')

train = limit(constructed, 'DD-MM-YYYY', 'DD-MM-YYYY')
test = limit(constructed, 'DD-MM-YYYY', 'DD-MM-YYYY')
````````

* the date used in _train_ is 03-01-2011 and 04-01-2011, so 1 day between
* the date used in _test_ is 1 day after each day in _train_ (04-01-2011 and 05-01-2011) 

---

## __Use in .ipynb__

````
import pandas as pd
from prophet import Prophet

df = pd.read_csv('../examples/example_wp_log_peyton_manning.csv')
df.head()

# Python
m = Prophet()
m.fit(df)

future = m.make_future_dataframe(periods=365)
future.tail()

forecast = m.predict(future)
forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()
`````

Plot

``
fig1 = m.plot(forecast)
``
![plot1](/images/m.plot_prophet.png)

``
fig2 = m.plot_components(forecast)
``

![plot2](/images/m.plot_components_prophet.png)


```
from prophet.plot import plot_plotly, plot_components_plotly

plot_plotly(m, forecast)
plot_components_plotly(m, forecast)
````

---

## __Comparision XGBoost, ARIMA and Prophet__

* __ARIMA__ is good for guessing the next future value 
* __ARIMA__ has highest MAE compared to _Prophet_ and _XGBoost_

* __Prophet__ is good for captioring seasons - e.g. for day and week
* __Prophet__ has the smallest MAE compared to _ARIMA_ and _XGBoost_ 
* To forecast for a whole month with only a month to learn from in advance is a very small case of possibilities - perhaps if you give more data to __Prophet__ it will capture the trend better.

* __XGBoost__ is good for estimating the most probable behavior of the curve.

![Comparision](/images/ARIMA_Prophet_XGBoost-Kaggle.png)

---

### __Sources__

* XGBoost, ARIMA and Prophet for Time Series: https://www.kaggle.com/furiousx7/xgboost-arima-and-prophet-for-time-series
* GitHub Facebook/prophet : https://github.com/facebook/prophet
* https://facebook.github.io/prophet/
* Quick Start: https://facebook.github.io/prophet/docs/quick_start.html