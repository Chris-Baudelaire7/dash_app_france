from dash import callback, Input, Output
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from data_preparation import *

from utils import *


@callback(
    Output('prtc', 'children'),
    Output('etblm', 'children'),
    Output('ps', 'children'),
    Input('city-picker', 'value'),
    allow_duplicate=True
)
def render_title(ville_choisie):
    return ville_choisie, ville_choisie, ville_choisie


@callback(Output('praticiens', 'data'), Output('praticiens', 'options'), Input('city-picker', 'value'))
def praticiens(ville_choisie):
    colonnes = ["Médecins généralistes", "Masseurs-kinésithérapeutes", "Dentistes", "Infirmiers",
                "Spécialistes ORL", "Ophtalmologistes", "Dermatologues", "Sage-femmes", "Pédiatres", "Gynécologues",
                "Pharmacies", "Ambulances"]
    labels = colonnes
    values = [float(df_sante[df_sante['ville'] == ville_choisie][colonne].iloc[0]) for colonne in colonnes]
    
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

    return [data, option(f"Praticiens à : {ville_choisie}")]

# Afficher le tableau des praticiens


@callback(Output('tableau_praticiens', 'data'), Output('tableau_praticiens', 'columns'), Input('city-picker', 'value'))
def tableau_praticiens(ville_choisie):
    colonnes = ["Médecins généralistes", "Masseurs-kinésithérapeutes", "Dentistes", "Infirmiers",
                "Spécialistes ORL", "Ophtalmologistes", "Dermatologues", "Sage-femmes", "Pédiatres", "Gynécologues",
                "Pharmacies", "Ambulances"]

    data, entete = tableau(df_sante, ville_choisie, colonnes)

    return data, entete


# Afficher le camembert des etablissements de sante


@callback(Output('etablissements', 'data'), Output('etablissements', 'options'), Input('city-picker', 'value'))
def etablissements(ville_choisie):
    colonnes = ["Urgences", "Etablissements de santé de court séjour", "Etablissements de santé de moyen séjour",
                "Etablissements de santé de long séjour", "Etablissement d'accueil du jeune enfant",
                "Maisons de retraite", "Etablissements pour enfants handicapés", "Etablissements pour adultes handicapés"]
    labels = colonnes
    values = [float(df_sante[df_sante['ville'] == ville_choisie][colonne].iloc[0]) for colonne in colonnes]
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

    return [data, option(f"Etalissements de Sante: {total}")]

# Afficher le tableau des etablissements


@callback(Output('tableau_etablissements', 'data'), Output('tableau_etablissements', 'columns'), Input('city-picker', 'value'))
def tableau_etablissements(ville_choisie):
    colonnes = ["Urgences", "Etablissements de santé de court séjour", "Etablissements de santé de moyen séjour",
                "Etablissements de santé de long séjour", "Etablissement d'accueil du jeune enfant",
                "Maisons de retraite", "Etablissements pour enfants handicapés", "Etablissements pour adultes handicapés"]

    data, entete = tableau(df_sante, ville_choisie, colonnes)

    return data, entete

# Graphes evolutions caf, apl, rsa, alloc


@callback(
    Output('presstations_sociales', 'data'), Output('presstations_sociales', 'options'), Input('city-picker', 'value')
)
def evolution_presstations_sociales(ville_choisie):
    x_axis = np.array(range(2009, 2018))
    y_caf = [
        df_sante[df_sante['ville'] == ville_choisie]["nbre allocataires (" + str(a) + ")"].iloc[0] for a in range(2009, 2018)
    ]
    y_rsa = [
        df_sante[df_sante['ville'] == ville_choisie]["nbre RSA (" + str(a) + ")"].iloc[0] for a in range(2009, 2018)
    ]
    y_apl = [
        df_sante[df_sante['ville'] == ville_choisie]["nbre APL (" + str(a) + ")"].iloc[0] for a in range(2009, 2018)
    ]
    y_alloc = [
        df_sante[df_sante['ville'] == ville_choisie]["nbre Alloc Familiales (" + str(a) + ")"].iloc[0] for a in range(2009, 2018)
    ]
    
    
    data = {
        'labels': x_axis,
        'datasets': [
            {
                'label': 'CAF',
                'data': y_caf,
                'backgroundColor': 'rgba(53, 162, 235, 1)',
                'borderColor': 'rgba(53, 162, 235, 1)',
                'borderWidth': 1
            },
            
            {
                'label': 'RSA',
                'data': y_rsa,
                'backgroundColor': 'rgba(75, 192, 192, 1)',
                'borderColor': 'rgba(75, 192, 192, 1)',
                'borderWidth': 1
            },
            
            {
                'label': 'APL',
                'data': y_apl,
                'borderColor': 'rgba(255, 99, 132, 1)',
                'backgroundColor': 'rgba(255, 99, 132, 1)',
                'borderWidth': 1
            },
            
            {
                'label': 'Allocation',
                'data': y_alloc,
                'backgroundColor': px.colors.qualitative.Plotly[4],
                'borderColor': px.colors.qualitative.Plotly[4],
                'borderWidth': 1
            }
        ]
    }

    return [data, option(f"Etalissements de Sante:")]




    
    
    