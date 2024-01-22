from dash import callback, Input, Output, html
import dash_ag_grid as dag
import folium
import os
from data_preparation import *


@callback(Output('table_infos', 'data'), Output('table_infos', 'columns'), Input('city-picker', 'value'))
def update_generales(ville_choisie):
    colonnes = df_infos.columns
    colonnes_off = ['Taux de chômage (2015)', 'Etablissement public de coopération intercommunale (EPCI)', 'lien',
                    "Pavillon bleu", "Ville d'art et d'histoire", "Ville fleurie", "Ville internet", 'ville']

    listeInfos = [info for info in colonnes if info not in colonnes_off]
    infos = {
        'intitule': listeInfos,
        'donnee': [df_infos[df_infos['ville'] == ville_choisie][col].iloc[0] for col in listeInfos]
    }

    table = pd.DataFrame(infos)
    data = table.to_dict("records")

    entete = {'id': 'intitule', 'name': "   "}, {
        'id': 'donnee', 'name': ville_choisie}

    return data, entete


@callback(Output('position-maps', 'children'), Input('city-picker', 'value'))
def update_location(ville_choisie):
    longitude = df_infos[df_infos['ville'] == ville_choisie]['Longitude'].iloc[0]
    latitude = df_infos[df_infos['ville'] == ville_choisie]['Latitude'].iloc[0]

    carte = folium.Map(location=(latitude, longitude), zoom_start=6)
    marker = folium.Marker(location=[latitude, longitude])
    marker.add_to(carte)

    fichier = "locations\\localisation_" + ville_choisie + ".html"

    if not os.path.isfile(fichier):
        carte.save(fichier)

    return html.Iframe(srcDoc=open(fichier, 'r').read(), width='100%', height='600')
