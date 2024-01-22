import dash
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
from dash import dcc, html, dash_table

from callbacks.info import *
from components import table


dash.register_page(__name__, path="/", order=1, name="Informations générales")

layout = html.Div(className="info", children=[
    
    html.H1("Informations générales sur les Villes de France", className="fw-bold"),
    
    dcc.Dropdown(
        id="city-picker",
        options=[{"label": city, "value": city} for city in list(df_infos.ville.unique())],
        value="Paris (75000)"
    ),
    
    html.Div(className="row mt-5", children=[
        
        html.Div(className="col-lg-5 div-table", children=[
            
            html.H6("Informations générales sur les Villes de France", className="fw-bold"),
            
            html.Small(
                """ 
                teams, players, coaches, etc. throughout each sports season. After all, a common passion connects people — and sports often bring people together. With so many opinions across different teams, what if we wanted to better understand the sentiment across
                """
            ),
            
            table("table_infos")
        
        ]),
        
        html.Div(className="col-lg-7 carte", id="position-maps")
    ])
])