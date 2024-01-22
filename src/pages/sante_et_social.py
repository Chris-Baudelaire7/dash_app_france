import dash
from dash import dcc, html
from dash_chartjs import ChartJs
from callbacks.sante_et_social import *
from components import table


dash.register_page(__name__, path="/sante-et-social", name="Santé et social")

layout = html.Div(className="sante-et-social", children=[
    
    html.H1("Santé et social en France", className="fw-bold toggle-button"),

    dcc.Dropdown(
        id="city-picker",
        options=[{"label": city, "value": city} for city in list(df_infos.ville.unique())],
        value="Paris (75000)"
    ),
    
    
    html.Div(className="mt-4 text-end", children=[
        html.H4("Santé", className="fw-bold text-end subtitle px-4 d-inline")
    ]),
    
    html.Div(className="mt-5 row align-items-center justify-content-center", children=[
        
        html.Div(className="col-md-8 carte", children=[
            html.Div(className="div-title-graph text-end", children=[
                html.Span("Praticiens", className="fw-bold title-graph"),
                html.Span(id="prtc", className="text-secondary")
            ]),
            ChartJs(id='praticiens', type='bar'),
        ]),
        
        html.Div(className="col-md-4", children=[
            table("tableau_praticiens")
        ])
        
    ]),
    
    
    html.Div(className="mt-5 row align-items-center justify-content-center", children=[

        html.Div(className="col-md-8 carte", children=[
            html.Div(className="div-title-graph text-end", children=[
                html.Span("Établissements de santé", className="fw-bold title-graph"),
                html.Span(id="etblm", className="text-secondary")
            ]),
            ChartJs(id='etablissements', type='bar'),
        ]),

        html.Div(className="col-md-4", children=[
            table("tableau_etablissements")
        ]),
    ]),
    
    
    
    html.Div(className="mt-5", children=[
        html.H4("Social", className="fw-bold subtitle px-4 d-inline")
    ]),
    
    html.Div(className="my-5 row justify-content-center", children=[
        
        html.Div(className="col-md-10 carte", children=[
            html.Div(className="div-title-graph text-end", children=[
                html.Span("Les prestations sociales", className="fw-bold title-graph"),
                html.Span(id="ps", className="text-secondary")
            ]),
            ChartJs(id='presstations_sociales', type='line'),
        ])
        
    ])
    
])


