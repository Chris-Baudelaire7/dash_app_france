from dash import callback, Input, Output
import numpy as np
import plotly.graph_objects as go
from data_preparation import *


# Camembert

def graphique_camembert(title, labels, values, total):

    traces = [
        go.Pie(
            labels=labels, values=values,
            textposition="auto", textinfo="label+percent",
            textfont=dict(size=12, family="serif"),
            insidetextorientation='radial',
        )
    ]

    return {
        'data': traces,
        'layout': go.Layout(
            title=f"<b>{title}</b><br> (Total: " + str(total) + ")",
            showlegend=False,
            margin=dict(l=0, r=0, b=0, t=60),
            font=dict(family="serif"),
            height=300,
        )
    }


# Tableau

def tableau(data, ville_choisie, colonnes):
    infos = {
        'intitule': colonnes,
        'donnee': [data[data['ville'] == ville_choisie][colonne].iloc[0] for colonne in colonnes]
    }
    
    table = pd.DataFrame(infos)
    data = table.to_dict('records')

    entete = [{'id': 'intitule', 'name': '   '}, {'id': 'donnee', 'name': ville_choisie.split('(')[0].strip()}]

    return data, entete


def layout(title):
    return go.Layout(
            height=390,
            margin=dict(l=0, r=0, b=30, t=40),
            font=dict(family="serif"),
            xaxis={'title': 'Années'},
            yaxis=dict(title="Nombre d'habitants"),
            hovermode='x',
            legend_orientation='h',
            
            title={
                "font": {"family": "serif", "size": 20, "color": "black"},
                "x": 0.98,
                "y": 0.93,
                "xanchor": "right",
                "yanchor": "top",
            },


        )
    
    
def option(title):
    return {
        'responsive': True,
        'plugins': {
            'legend': {
                'position': "bottom",
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
                'display': False,
                'title': {
                    'display': True,
                    'text': "Nombre d'habitants"
                }
            }
        }
    }
    
    
def option_pie(title):
    return {
        'responsive': True,
        'plugins': {
            'legend': {
                'position': "bottom",
            },
            'datalabels': {
                'display': False
            }
        },
    }
    

def option_radar(title):
    return {
        'responsive': True,
        'plugins': {
            'legend': {
                'position': "bottom",
            },
            'datalabels': {
                'display': False
            }
        },
    }
