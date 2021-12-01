from math import e
import pandas as pd
import plotly.express as px

import dash 
import dash_core_components as dcc
import plotly.graph_objects as go
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

df1h1f = pd.read_csv('data/forecasts_1h_1f_sarima.csv')
df1h6f = pd.read_csv('data/forecasts_1h_6f_sarima.csv')
df6h1f = pd.read_csv('data/forecasts_6h_1f_sarima.csv')
df6h6f = pd.read_csv('data/forecasts_6h_6f_sarima.csv')

def make_plots_1h1f():
    fig_1h1f = px.line(df1h1f, x="dt_start_utc", y='predicted')
    fig_1h1f = px.line(df1h1f, x="dt_start_utc", y='imbalance_price_target')
    return fig_1h1f

def make_plots_1h6f():
    fig_1h6f = px.line(df1h6f, x="dt_start_utc", y='predicted')
    fig_1h6f = px.line(df1h6f, x="dt_start_utc", y='imbalance_price_target')
    return fig_1h6f

def make_plots_6h1f():
    fig_6h1f = px.line(df6h1f, x="dt_start_utc", y='predicted')
    fig_6h1f = px.line(df6h1f, x="dt_start_utc", y='imbalance_price_target')
    return fig_6h1f

def make_plots_6h6f():
    fig_6h6f = px.line(df6h6f, x="dt_start_utc", y='predicted')
    fig_6h6f = px.line(df6h6f, x="dt_start_utc", y='imbalance_price_target')
    return fig_6h6f



app.layout = html.Div(
    [
    html.Div(children=[
        html.Label('Dropdown'),
        dcc.Dropdown(
            id='forecast_dropdown',
            options=[
                {'label': 'SARIMA 1 Hour 1 Forecast', 'value': 'sarima_1h1f'},
                {'label': 'SARIMA 1 Hours 6 Forcasts', 'value': 'sarima_1h6f'},
                {'label': 'SARIMA 6 Hours 1 Forecast', 'value': 'sarima_6h1f'},
                {'label': 'SARIMA 6 Hours 6 Forecasts', 'value': 'sarima_6h1f'},
                {'label': 'Prophet 1 Hour', 'value': 'prophet_1'},
                {'label': 'Prophet 6 Hours', 'value': 'prophet_6'}]),
    html.Div(id="forecast"),   
    ]
)])

@app.callback(
    Output('forecast', 'children'),
    Input('forecast_dropdown', 'value')
)
def update_output(value):
    if value=='sarima_1h1f': 
        fig_1h1f = make_plots_1h1f()
        return dcc.Graph(figure=fig_1h1f)
    elif value=='sarima_1h6f': 
        fig_1h6f = make_plots_1h6f()
        return dcc.Graph(figure=fig_1h6f)
    elif value=='sarima_6h1f': 
        fig_6h1f = make_plots_6h1f()
        return dcc.Graph(figure=fig_6h1f)
    elif value=='sarima_6h6f':
        fig_6h6f = make_plots_6h6f()
        return dcc.Graph(figure=fig_6h6f)
    

if __name__ == '__main__':
    app.run_server(debug=True)