from dash import callback, Input, Output, html
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from dash_iconify import DashIconify
import dash_mantine_components as dmc

from data_preparation import *


@callback(Output("notifications-container", "children"), Input("city-picker", "value"), prevent_initial_call=True)
def show(ville):
    
    if ville == "Paris (75000)":
        return dmc.Notification(
            title="Paris: Capitale de la France",
            id="simple-notify",
            action="show",
            message="La plus belle ville de FFrance",
            icon=DashIconify(icon="mdi:eiffel-tower"),
        )
        
    if ville == "Marseille (13000)":
        return dmc.Notification(
            title="Hey there!",
            id="simple-notify",
            action="show",
            message="Notifications in Dash, Awesome!",
            icon=DashIconify(icon="ic:round-celebration"),
        )
