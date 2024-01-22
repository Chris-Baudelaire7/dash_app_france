from dash import callback, Input, Output, html
from data_preparation import *
import base64
from operator import itemgetter


@callback(Output('elections', 'children'), Input('city-picker', 'value'))
def elections(ville_choisie):
    liste_candidats = df_candidats['candidat']

    donnees = []

    for candidat in liste_candidats:
        parti = df_candidats[df_candidats['candidat'] == candidat]['parti'].iloc[0]
        pourcentage = float(df_elections[df_elections['ville'] == ville_choisie][candidat].iloc[0])
        photo = df_candidats[df_candidats['candidat'] == candidat]['photo'].iloc[0]
        color = df_candidats[df_candidats['candidat']== candidat]['color'].iloc[0]

        donnees.append([pourcentage, candidat, photo, parti, color])

    donnees = sorted(donnees, reverse=True, key=itemgetter(0))

    liste_div = []

    for candidat in donnees:
        image_filename = "candidats/" + candidat[2]
        encoded_image = base64.b64encode(open(image_filename, 'rb').read())
        liste_div.append(
            html.Div([
                html.Div([
                    html.Img(
                        src='data:image/png;base64,{}'.format(encoded_image.decode()))
                ], style={'backgroundColor': candidat[-1],
                          'width': str(candidat[0]) + "%",
                          'height': '100%',
                          'fontSize': '20px',
                          'verticalAlign': 'top',
                          'border': '1px solid grey'}),
                html.Div([
                    html.Div([
                        html.P(candidat[1])
                    ], style={'display': 'inline-block', 'width': '30%', 'fontWeight': 'bold', 'verticalAlign': 'top'}),
                    html.Div([
                        html.P(candidat[3])
                    ], style={'display': 'inline-block', 'width': '50%', 'fontWeight': 'italic', 'fontSize': '12px', 'verticalAlign': 'top'}),
                    html.Div([
                        html.P(str(candidat[0]) + "%")
                    ], style={'display': 'inline-block', 'width': '20%', 'fontWeight': 'bold', 'textAlign': 'right'}),
                ], style={'width': '100%',
                          'position': 'absolute',
                          'height': '100%',
                          'top': 0,
                          'left': 0,
                          'paddingLeft': '60px',
                          'border': '1px solid' + candidat[-1]})
            ], style={'height': '50px', 'position': 'relative', 'marginBottom': '5px'})
        )

    return liste_div
