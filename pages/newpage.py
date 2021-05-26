from joblib import load
pipeline = load('assets/penguin_model.joblib')

import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app

column1 = dbc.Col(
    [
        dcc.Markdown('## Predictions', className='mb-5'), 
        dcc.Markdown('#### Penguin Mass (g)'), 
        dcc.Slider(
            id='mass', 
            min=2700, 
            max=6300, 
            step=500, 
            value=4200, 
            marks={n: str(n) for n in range(2700,6300,500)}, 
            className='mb-5', 
        ), 
        dcc.Markdown('#### Island'), 
        dcc.Dropdown(
            id='island', 
            options = [
                {'label': 'Biscoe', 'value': 'Biscoe'}, 
                {'label': 'Dream', 'value': 'Dream'}, 
                {'label': 'Torgersen', 'value': 'Torgersen'}, 
            ], 
            value = 'Biscoe', 
            className='mb-5', 
        ), 
    ],
    md=4,
)

column2 = dbc.Col(
    [
        html.H2('Penguin Species', className='mb-5'), 
        html.Div(id='prediction-content', className='lead')
    ]
)

import pandas as pd

@app.callback(
    Output('prediction-content', 'children'),
    [Input('mass', 'value'), Input('island', 'value')],
)
def predict(mass, island):
    df = pd.DataFrame(
        columns=['mass', 'island'], 
        data=[[mass, island]]
    )
    y_pred = pipeline.predict(df)[0]
    print(y_pred)
    return y_pred + ' Penguin'

layout = dbc.Row([column1, column2])