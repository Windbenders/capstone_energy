## Notes: Time series split 
* [Documentation](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TimeSeriesSplit.html)
* Syntax:

`TimeSeriesSplit (n_splits=5, *, max_train_size=None, test_size=None, gap=0)`

* successive training sets are supersets of those that come before them
* surplus data to the first training partition
* **actual splitting**:

*"This was the trickiest part as a newbie. Straight from the docs
If you only have experience with CV splits this way of making the splits might seem foreign. Fret not.for train_index, test_index in tss.split(X):

    X_train, X_test = X.iloc[train_index, :], X.iloc [test_index,:]
    y_train, y_test = y.iloc[train_index], y.iloc[test_index]
    
* [Short and straightforward example](https://medium.com/@dcamarena0229/time-series-split-with-scikit-learn-de7ec17d69cd)

<br />

## Notes: Inner forecast
* Don't know if I got i right couldn't find information on this

## Notes: Forecast with Arima [(source)](https://medium.com/@cdabakoglu/time-series-forecasting-arima-lstm-prophet-with-python-e73a750a9887)
* Finding best model & parameters with auto_arima: \
`auto_arima(df['Monthly beer production'], seasonal=True, m=12,max_p=7, max_d=5,max_q=7, max_P=4, max_D=4,max_Q=4).summary()`

* splitting into train and test data set: \
`train_data = df[:len(df)-12]` \
`test_data = df[len(df)-12:]`

* assigning model: \
`arima_model = SARIMAX(train_data['Monthly beer production'], order = (2,1,1), seasonal_order = (4,0,3,12))`

* fitting model:\
`arima_result = arima_model.fit()
arima_result.summary()`

* assigning predictions: \
`arima_pred = arima_result.predict(start = len(train_data), end = len(df)-1, typ="levels").rename("ARIMA Predictions")arima_pred`

* getting metrics: \
`arima_rmse_error = rmse(test_data['Monthly beer production'], arima_pred)
arima_mse_error = arima_rmse_error**2
mean_value = df['Monthly beer production'].mean()` \
`print(f'MSE Error: {arima_mse_error}\nRMSE Error: {arima_rmse_error}\nMean: {mean_value}')`