from dash import callback, Input, Output
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from data_preparation import *
import random
import dash
from utils import *

dash._dash_renderer._set_react_version("18.2.0")


plotly_orange = px.colors.qualitative.Plotly[4]
plotly_blue = px.colors.qualitative.Plotly[0]


@callback(
    Output('pop', 'children'), 
    Output('nd', 'children'),
    Output('etr', 'children'),
    Output('imig', 'children'),
    Input('city-picker', 'value')
)
def render_title(ville_choisie):    
    return ville_choisie, ville_choisie, ville_choisie, ville_choisie


@callback(Output('chart-1', 'data'), Output('chart-1', 'options'), Input('city-picker', 'value'))
def display_output(ville_choisie):
    x_axis = np.array(range(2006, 2016))
    y_axis = [
        df_demo[df_demo['ville'] == ville_choisie]["nbre habitants (" + str(annee) + ")"].iloc[0] for annee in range(2006, 2016)
    ]

    data1 = {
        'labels': x_axis,
        'datasets': [
            {
                'label': "Nombre d'habitants",
                'fill': False,
                'backgroundColor': 'rgba(53, 162, 235,0.2)',
                'borderColor': 'rgba(53, 162, 235,1)',
                'data': y_axis,
                "tension": 0.3
            }
        ]
    }

    return [data1, option("Évolution du nombre d'habitants à " + ville_choisie)]


@callback(Output('naissances_deces', 'data'), Output('naissances_deces', 'options'), Input('city-picker', 'value'))
def display_output(ville_choisie):
        
    x_axis = np.array(range(1999, 2017))
    y_axis_naissances = [
        df_demo[df_demo["ville"] == ville_choisie]["nbre naissances (" + str(a) + ")"].iloc[0] for a in range(1999, 2017)
    ]
    y_axis_deces = [
        df_demo[df_demo["ville"] == ville_choisie]["nbre deces (" + str(a) + ")"].iloc[0] for a in range(1999, 2017)
    ]

    data1 = {
        'labels': x_axis,
            'datasets': [
                {
                    'label': 'Nombre de naissance',
                    'fill': False,
                    'backgroundColor': 'rgba(53, 162, 235, 1)',
                    'borderColor': 'rgba(53, 162, 235, 1)',
                    'data': y_axis_naissances,
                    "tension": 0.3
                },
                {
                    'label': 'Nombre de décès',
                    'fill': False,
                    'backgroundColor': plotly_orange,
                    'borderColor': plotly_orange,
                    'data': y_axis_deces,
                    "tension": 0.3
                },
                
            ]
        }

    options1 = {
            'responsive': True,
            'plugins': {
                'legend': {
                    'position': "bottom",
                },
                'zoom': {
                    'zoom': {
                        'wheel': {
                            'enabled': True
                        },
                        'mode': 'xy'
                    }
                },
                'datalabels': {
                    'display': False
                }
            },
            'interaction': {
                'mode': 'index',
                'intersect': False
            },
            'scales': {
                'x': {
                    'display': True,
                    'title': {
                        'display': True,
                        'text': 'Années'
                    }
                },
                'y': {
                    'ticks': {
                        'beginAtZero': True
                    },
                    'display': False,
                    'title': {
                        'display': True,
                        'text': "Nombre d'habitants"
                    }
                }
            }
        }    

    return [data1, options1]
    


@callback(Output("hommes_femmes", "data"), Output("hommes_femmes", "options"), Input('city-picker', 'value'))
def repartition_HF(ville_choisie):
    nb_hommes = df_demo[df_demo['ville'] == ville_choisie]["Hommes"].iloc[0]
    nb_femmes = df_demo[df_demo['ville'] == ville_choisie]["Femmes"].iloc[0]

    labels = ['Hommes', 'Femmes']
    values = [float(nb_hommes), float(nb_femmes)]
    total = sum(values)
    
    data = {
        'labels': labels,
        'datasets': [
            {
                'label': 'Dataset 1',
                'data': values,
                'backgroundColor': [plotly_blue, plotly_orange],
                'borderColor': [plotly_blue, plotly_orange],
                'borderWidth': 1
            }
        ]
    }

    return [data, option_pie(f"Repartition Hommes/Femmes: {total}")]



@callback(Output("ages", "data"), Output("ages", "options"), Input('city-picker', 'value'))
def repartition_ages(ville_choisie):
    colonnes = ["Moins de 15 ans", "15 - 29 ans", "30 - 44 ans", "45 - 59 ans", "60 - 74 ans", "75 ans et plus"]

    labels = colonnes
    values = [float(df_demo[df_demo['ville'] == ville_choisie][colonne].iloc[0]) for colonne in colonnes]
    total = sum(values)
    
    data = {
        'labels': labels,
        'datasets': [
            {
                'label': 'Dataset 1',
                'data': values,
                'backgroundColor': px.colors.qualitative.Plotly,
                'borderColor': px.colors.qualitative.Plotly,
                'borderWidth': 1
            }
        ]
    }

    return [data, option_pie(f"Repartition par Tranches d'ages: {total}")]
    

# Tableau des repartitions hommes/femmes et tranches d'ages


@callback(Output('repartitions', 'data'), Output('repartitions', 'columns'), Input('city-picker', 'value'))
def table_repartitions(ville_choisie):
    colonnes = ["Hommes", "Femmes", "Moins de 15 ans", "15 - 29 ans", "30 - 44 ans", "45 - 59 ans", "60 - 74 ans", "75 ans et plus"]

    data, entete = tableau(df_demo, ville_choisie, colonnes)

    return data, entete


@callback(Output('familles', 'data'), Output('familles', 'options'), Input('city-picker', 'value'))
def repartition_familles(ville_choisie):
    colonnes = ["Familles monoparentales", "Couples sans enfant", "Couples avec enfant",
                "Familles sans enfant", "Familles avec un enfant", "Familles avec deux enfants", "Familles avec trois enfants",
                "Familles avec quatre enfants ou plus"]

    labels = colonnes
    values = [float(df_demo[df_demo['ville'] == ville_choisie][colonne].iloc[0]) for colonne in colonnes]
    total = sum(values)
    
    data = {
        'labels': labels,
        'datasets': [
            {
                'data': values,
                'backgroundColor': px.colors.qualitative.Plotly,
                'borderColor': px.colors.qualitative.Plotly,
                'borderWidth': 1
            }
        ]
    }
    
    options = {
            'responsive': True,
            'plugins': {
                'legend': {
                    'position': "bottom",
                },
                'datalabels': {
                    'display': False
                },
            },
            'scales': {
                'y': {
                    'display': False
                }
            }
        }

    return [data, options]
    

# Repartition du statut marital

@callback(Output('statut_marital', 'data'), Output('statut_marital', 'options'), Input('city-picker', 'value'))
def repartition_statut_marital(ville_choisie):
    colonnes = ["Personnes célibataires", "Personnes mariées", "Personnes divorcées", "Personnes veuves"]

    labels = colonnes
    values = [float(df_demo[df_demo['ville'] == ville_choisie][colonne].iloc[0]) for colonne in colonnes]
    total = sum(values)
    
    data = {
        'labels': labels,
        'datasets': [
            {
                'label': 'Dataset 1',
                'data': values,
                'backgroundColor': px.colors.qualitative.Plotly,
                'borderColor': px.colors.qualitative.Plotly,
                'borderWidth': 1
            }
        ]
    }

    return [data, option_pie(f"Status Marital: {total}")]

    
# Tableau 2 des repartitions


@callback(Output('repartitions_2', 'data'), Output('repartitions_2', 'columns'), Input('city-picker', 'value'))
def table_repartitions(ville_choisie):
    colonnes = ["Familles monoparentales", "Couples sans enfant", "Couples avec enfant",
                "Familles sans enfant", "Familles avec un enfant", "Familles avec deux enfants", "Familles avec trois enfants",
                "Familles avec quatre enfants ou plus", "Personnes célibataires", "Personnes mariées", "Personnes divorcées",
                "Personnes veuves"]

    data, entete = tableau(df_demo, ville_choisie, colonnes)

    return data, entete


@callback(
    Output('evolution_etrangers', 'data'),  Output('evolution_etrangers', 'options'),
    Output('evolution_immigres', 'data'),  Output('evolution_immigres', 'options'),
    Input('city-picker', 'value')
)
def evolution_etrangers_immigres(ville_choisie):
    x_axis = np.array(range(2006, 2016))
    y_axis_etrangers = [
        df_demo[df_demo['ville'] == ville_choisie]["nbre étrangers (" + str(a) + ")"].iloc[0] for a in range(2006, 2016)
    ]
    y_axis_immigres = [
        df_demo[df_demo['ville'] == ville_choisie]["nbre immigrés (" + str(a) + ")"].iloc[0] for a in range(2006, 2016)
    ]

    ville_choisie = ville_choisie.split('(')[0].strip()
    
    data_etrangers = {
        'labels': x_axis,
        'datasets': [
            {
                'label': "Nombre d'habitants",
                'fill': False,
                'backgroundColor': 'rgba(53, 162, 235,0.2)',
                'borderColor': 'rgba(53, 162, 235,1)',
                'data': y_axis_etrangers,
                "tension": 0.3
            }
        ]
    }
    
    data_immigres = {
        'labels': x_axis,
        'datasets': [
            {
                'label': "Nombre d'habitants",
                'fill': False,
                'backgroundColor': 'rgba(53, 162, 235,0.2)',
                'borderColor': 'rgba(53, 162, 235,1)',
                'data': y_axis_immigres,
                "tension": 0.3
            }
        ]
    }

    return [
        data_etrangers, option("Évolution du nombre d'habitants à " + ville_choisie), 
        data_immigres, option("Évolution du nokmbre d'habitants à " + ville_choisie)
    ]



@callback(Output("repartitions_etrangers_HF","data"), Output("repartitions_etrangers_HF","options"), Input('city-picker','value'))
def repartition_HF_Etrangers(ville_choisie):
    nb_hommes = df_demo[df_demo['ville'] == ville_choisie]["Hommes étrangers"].iloc[0]
    nb_femmes = df_demo[df_demo['ville'] == ville_choisie]["Femmes étrangères"].iloc[0]

    labels = ["Hommes étrangers","Femmes étrangères"]
    values = [float(nb_hommes), float(nb_femmes)]
    total = sum(values)
    
    data = {
        'labels': labels,
        'datasets': [
            {
                'label': 'Dataset 1',
                'data': values,
                'backgroundColor': px.colors.qualitative.Plotly,
                'borderColor': px.colors.qualitative.Plotly,
                'borderWidth': 1
            }
        ]
    }

    return [data, option_pie(f"Population Etrangere | Hommes/Femmes: {total}")]
    


# Camembert Ages etrangers


@callback(Output('repartitions_etrangers_ages', 'data'), Output('repartitions_etrangers_ages', 'options'), Input('city-picker', 'value'))
def repartition_ages(ville_choisie):
    colonnes = ["Moins de 15 ans étrangers","15-24 ans étrangers","25-54 ans étrangers","55 ans et plus étrangers"]

    labels = colonnes
    values = [float(df_demo[df_demo['ville'] == ville_choisie][colonne].iloc[0]) for colonne in colonnes]
    total = sum(values)
    
    data = {
        'labels': labels,
        'datasets': [
            {
                'label': 'Dataset 1',
                'data': values,
                'backgroundColor': px.colors.qualitative.Plotly,
                'borderColor': px.colors.qualitative.Plotly,
                'borderWidth': 1
            }
        ]
    }

    return [data, option_pie(f"Repartition par Tranches d'ages des Etrangers: {total}")]
    


# Tableau repartitions etrangers
@callback(Output('tableau_etrangers','data'), Output('tableau_etrangers','columns'), Input('city-picker','value'))
def table_repartitions(ville_choisie):
    colonnes = ["Hommes étrangers","Femmes étrangères","Moins de 15 ans étrangers",
                "15-24 ans étrangers","25-54 ans étrangers","55 ans et plus étrangers"]

    data, entete = tableau(df_demo, ville_choisie, colonnes)

    return data, entete



# Camembert HF immigres
@callback(Output("repartitions_immigres_HF", "data"), Output("repartitions_immigres_HF", "options"), Input('city-picker', 'value'))
def repartition_HF_Etrangers(ville_choisie):
    nb_hommes = df_demo[df_demo['ville'] ==
                        ville_choisie]["Hommes immigrés"].iloc[0]
    nb_femmes = df_demo[df_demo['ville'] ==
                        ville_choisie]["Femmes immigrées"].iloc[0]

    labels = ["Hommes immigrés", "Femmes immigrées"]
    values = [float(nb_hommes), float(nb_femmes)]
    total = sum(values)
    
    data = {
        'labels': labels,
        'datasets': [
            {
                'label': 'Dataset 1',
                'data': values,
                'backgroundColor': px.colors.qualitative.Plotly,
                'borderColor': px.colors.qualitative.Plotly,
                'borderWidth': 1
            }
        ]
    }

    return [data, option_pie(f"Population Immigree | Hommes/Femmes: {total}")]



# Camembert Ages immigres


@callback(Output('repartitions_immigres_ages', 'data'), Output('repartitions_immigres_ages', 'options'), Input('city-picker', 'value'))
def repartition_ages(ville_choisie):
    colonnes = ["Moins de 15 ans immigrés", "15-24 ans immigrés",
                "25-54 ans immigrés", "55 ans et plus immigrés"]

    labels = colonnes
    values = [float(df_demo[df_demo['ville'] == ville_choisie]
                    [colonne].iloc[0]) for colonne in colonnes]
    total = sum(values)
    
    data = {
        'labels': labels,
        'datasets': [
            {
                'label': 'Dataset 1',
                'data': values,
                'backgroundColor': px.colors.qualitative.Plotly,
                'borderColor': px.colors.qualitative.Plotly,
                'borderWidth': 1
            }
        ]
    }

    return [data, option_pie(f"Repartition par Tranches d'ages des Immigres: {total}")]
    


# Tableau repartitions immigres


@callback(Output('tableau_immigres', 'data'), Output('tableau_immigres', 'columns'), Input('city-picker', 'value'))
def table_repartitions(ville_choisie):
    colonnes = ["Hommes immigrés", "Femmes immigrées", "Moins de 15 ans immigrés", "15-24 ans immigrés",
                "25-54 ans immigrés", "55 ans et plus immigrés"]

    data, entete = tableau(df_demo, ville_choisie, colonnes)

    return data, entete
