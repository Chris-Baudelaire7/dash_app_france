import dash
from flask import Flask
from dash import html, Dash, dcc
import dash_bootstrap_components as dbc
import dash_admin_components as dac
import dash_mantine_components as dmc

from components import *


app_params = {
    "server": Flask(__name__),
    "title": "Chris Baudelaire - Data - Portfolio",
    "use_pages": True,
    "update_title": "Wait a moment...",
    "url_base_pathname": "/",
    "external_stylesheets": [dbc.themes.CYBORG, dbc.icons.BOOTSTRAP],
    "suppress_callback_exceptions": True,
    "meta_tags": [{'name': 'viewport', 'content': 'width=device-width, initial-scale=1.0'}]
}

server_params = {"debug": True, "port": 11999}


app = Dash(__name__, **app_params)

server = app.server

app.layout = dac.Page(id="app-root", className="app-root px-0 px-md-4", children=[
    
    dmc.NotificationsProvider([
        
            
        navbar, sidebar, controlbar,
        
        html.Div(id="notifications-container"),

        dac.Body(className="page bg-white", children=[
            dash.page_container
        ]),
        
        footer,
            
    ])
    
])


if __name__ == '__main__':
    app.run_server(**server_params)
