import dash
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
from dash import dcc, html

from callbacks.election import *
from components import table


dash.register_page(__name__, path="/elections", name="Élections")

layout = html.Div(className="elections", children=[
    
    html.H1("Élections européennes de 2019 en France", className="fw-bold toggle-button"),

    dcc.Dropdown(
        id="city-picker",
        options=[{"label": city, "value": city} for city in list(df_infos.ville.unique())],
        value="Paris (75000)"
    ),
    
    html.Div(className="row mt-5", children=[
        
        html.Div(className="col-md-12 pct", children=[
            html.Div(className="pct", id="elections"),
        ]),
        
        html.Div(className="col-md-5", children=[

        ])
        
    ])
    
])