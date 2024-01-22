import dash
from dash import dcc, html
from dash_chartjs import ChartJs
import dash_bootstrap_components as dbc
from callbacks.demographie import *
from callbacks.other_callbacks import *
from components import *


dash.register_page(__name__, path="/demographie", name="Démographie en France")

layout = html.Div(className="info", children=[
    
    html.H1("Démographie en France", className="fw-bold toggle-button"),    

    select,
    
    html.Div(className="mt-4 text-end", children=[
        html.H4("Population Française", className="fw-bold text-end subtitle px-4 d-inline")
    ]),
    
    html.Div(className="mt-5 row g-5 populaion justify-content-center", children=[
                
        html.Div(className="col-lg-6 carte", children=[
            html.Div(className="div-title-graph text-end", children=[
                html.Span("Évolution du nombre d'habitants", className="fw-bold title-graph"),
                html.Span(id="pop", className="text-secondary")
            ]),
            ChartJs(id='chart-1', type='line')
        ]),
                
        html.Div(className="col-lg-6 carte", children=[
            html.Div(className="div-title-graph text-end", children=[
                html.Span("Évolution des naissances et décès", className="fw-bold title-graph"),
                html.Span(id="nd", className="text-secondary")
            ]),
            ChartJs(id='naissances_deces', type='line')
        ]),
        
    ]),
    
    
    html.Div(className="mt-4 row g-5 align-items-center justify-content-center", children=[

        html.Div(className="col-lg-3 carte", children=[
            html.Div(className="div-title-graph text-center", children=[
                html.Span("Repartition Hommes/Femmes", className="fw-bold title-graph"),
                html.Span("(Total: 4568)", className="text-secondary")
            ]),
            ChartJs(id='hommes_femmes', type='doughnut')
        ]),

        html.Div(className="col-lg-4 carte", children=[
            html.Div(className="div-title-graph text-center", children=[
                html.Span("Repartition par Tranches d'ages", className="fw-bold title-graph"),
                html.Span("(Total: 4568)", className="text-secondary")
            ]),
            ChartJs(id='ages', type='doughnut')
        ]),
        
        
        html.Div(className="col-lg-5", children=[
            table("repartitions")
        ]),

    ]),
    
    
    
    html.Div(className="mt-4 row align-items-center justify-content-center", children=[

        html.Div(className="col-lg-3 carte", children=[
            html.Div(className="div-title-graph text-center", children=[
                html.Span("Status Marital", className="fw-bold title-graph"),
                html.Span("(Total: 4568)", className="text-secondary")
            ]),
            ChartJs(id='statut_marital', type='doughnut')
        ]),
        
        html.Div(className="col-lg-4 carte", children=[
            html.Div(className="div-title-graph text-end", children=[
                html.Span("Familles", className="fw-bold title-graph"),
                html.Span("Données srapées du site le journal du net", className="text-secondary")
            ]),
            ChartJs(id='familles', type='polarArea')
        ]),

        html.Div(className="col-lg-5", children=[
            table("repartitions_2")
        ]),

    ]),
    
    
    
    html.Div(className="mt-5 text-start", children=[
        html.H4("Population Étrangère", className="fw-bold text-end subtitle px-4 d-inline")
    ]),
    
    html.Div(className="mt-5 row justify-content-center", children=[

        html.Div(className="col-11 carte", children=[
            html.Div(className="div-title-graph text-end", children=[
                html.Span("Évolution du nombre d'étrangers", className="fw-bold title-graph"),
                html.Span(id="etr", className="text-secondary")
            ]),
            ChartJs(id='evolution_etrangers', type='line')
        ])

    ]),
    
    
    html.Div(className="mt-4 row align-items-center justify-content-center", children=[

        html.Div(className="col-lg-3 carte", children=[
            html.Div(className="div-title-graph text-center", children=[
                html.Span("Repartition des familles ", className="fw-bold title-graph"),
                html.Span("(Total: 4568)", className="text-secondary")
            ]),
            ChartJs(id='repartitions_etrangers_HF', type='doughnut')
        ]),

        html.Div(className="col-lg-4 carte", children=[
            html.Div(className="div-title-graph text-center", children=[
                html.Span("Repartition des familles ", className="fw-bold title-graph"),
                html.Span("(Total: 4568)", className="text-secondary")
            ]),
            ChartJs(id='repartitions_etrangers_ages', type='doughnut')
        ]),

        html.Div(className="col-lg-5", children=[
            table("tableau_etrangers")
        ]),

    ]),
    
    
    html.Div(className="mt-5 text-end", children=[
        html.H4("Population Immigrées", className="fw-bold text-end subtitle px-4 d-inline")
    ]),

    html.Div(className="mt-5 row justify-content-center", children=[

        html.Div(className="col-9 carte", children=[
            html.Div(className="div-title-graph text-end", children=[
                html.Span("Évolution du nombre d'imigrés", className="fw-bold title-graph"),
                html.Span(id="imig", className="text-secondary")
            ]),
            ChartJs(id='evolution_immigres', type='line')
        ])

    ]),
    
    
    html.Div(className="mt-4 row align-items-center justify-content-center mb-5", children=[

        html.Div(className="col-lg-3 carte", children=[
            html.Div(className="div-title-graph text-center", children=[
                html.Span("Repartition des familles ", className="fw-bold title-graph"),
                html.Span("(Total: 4568)", className="text-secondary")
            ]),
            ChartJs(id='repartitions_immigres_HF', type='doughnut')
        ]),

        html.Div(className="col-lg-4 carte", children=[
            html.Div(className="div-title-graph text-center", children=[
                html.Span("Repartition des familles ", className="fw-bold title-graph"),
                html.Span("(Total: 4568)", className="text-secondary")
            ]),
            ChartJs(id='repartitions_immigres_ages', type='doughnut')
        ]),

        html.Div(className="col-lg-5", children=[
            table("tableau_immigres")
        ]),

    ]),
    
])


# 
