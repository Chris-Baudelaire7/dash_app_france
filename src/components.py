import dash_admin_components as dac
from dash import html, dcc, dash_table
import dash_mantine_components as dmc
from dash_iconify import DashIconify
import dash

from data_preparation import *





right_ui = dac.NavbarDropdown(
    badge_label="!",
    badge_color="danger",
    src="https://quantee.ai",
   	header_text="2 Items",
    children=[
        dac.NavbarDropdownItem(
            children="message 1",
            date="today"
        ),
        dac.NavbarDropdownItem(
            children="message 2",
            date="yesterday"
        ),
    ]
)


navbar = dac.Navbar(className="nav-bar", fixed=True, color="white", text="Analyse Statistique des données et visualisation", children=right_ui)


subitems = [dac.SidebarMenuSubItem(id='tab_gallery_1',
                                   label='Gallery 1',
                                   icon='arrow-circle-right',
                                   badge_label='Soon',
                                   badge_color='success'),
            dac.SidebarMenuSubItem(id='tab_gallery_2',
                                   label='Gallery 2',
                                   icon='arrow-circle-right',
                                   badge_label='Soon',
                                   badge_color='success')
            ]

sidebar = dac.Sidebar(
	dac.SidebarMenu(
		[
			dac.SidebarHeader(children="Information générales"),
			dcc.Link(href="/", className="nav_link", children=[dac.SidebarMenuItem(id='geo', label=' Infos géographique', icon='box'),]),
            dcc.Link(href="/demographie", className="nav_link", children=[dac.SidebarMenuItem(id='dem', label=' Démographie', icon='id-card'),]),
            dcc.Link(href="/sante-et-social", className="nav_link", children=[dac.SidebarMenuItem(id='dedm', label='Santé et social', icon='image'),]),
            dcc.Link(href="/elections", className="nav_link", children=[dac.SidebarMenuItem(id='deem', label='Élection 2019', icon='image'),]),
            
            dac.SidebarHeader(children="Guerre en France"),
			dac.SidebarMenuItem(id='tab_basnic_boxes', label='Conflits politique', icon='desktop'),
			dac.SidebarMenuItem(id='tabn_value_boxes', label='Terrorisme', icon='suitcase'),
   
			dac.SidebarHeader(children="Pandémie de Covid-19"),
			dac.SidebarMenuItem(id='tab_basic_boxes', label='Basic boxes', icon='desktop'),
			dac.SidebarMenuItem(id='tab_value_boxes', label='Value/Info boxes', icon='suitcase'),
   
			dac.SidebarHeader(children="Gallery"),
			dac.SidebarMenuItem(label='Galleries', icon='cubes', children=subitems),
   
		]
	),
    title='Chris Baudelaire .K',
	skin="light",
    color="danger",
   	brand_color="light-grey",
    url="https://www.linkedin.com/in/chris-baudelaire-k-8284731a1/",
    src='/assets/cccb-6.png',
    elevation=3,
    opacity=0.9
)


controlbar = dac.Controlbar(
    [
        html.Br(),
        html.P("Slide to change graph in Basic Boxes"),
        dcc.Slider(
            id='controlbar-slider',
            min=10,
            max=20,
            step=1,
            value=20
        )
    ],
    title="My right sidebar",
    skin="light"
)

# Footer
footer = dac.Footer(right_text="2024", children=[
    html.Small(className="fw-bold", children=[
        html.Span("@"),
        html.Span("Analytics"),
        html.Span("Paper", className="text-danger"),
        html.Span(" | Powered By Plotly/Dash", className="text")
    ])
])


# select = dmc.Select(
#     id="city-picker",
#     data=list(df_infos.ville.unique()),
#     value="Paris (75000)",
#     label="Selectionner une ville",
#     icon=DashIconify(icon="radix-icons:magnifying-glass"),
#     rightSection=DashIconify(icon="radix-icons:chevron-down"),
#     description="Toutes les villes de France",
#     dropdownPosition="flip",
#     filterDataOnExactSearchMatch=True,
#     initiallyOpened=True,
#     nothingFound="nothingFound",
#     required=True,
#     selectOnBlur=True,
#     shadow=True,
#     switchDirectionOnFlip=True,
#     transition="skew-down",
#     transitionDuration=400,
#     withAsterisk=True,
#     style={"fontFamily": "serif", "width": 500},
# )



def table(idx):
    return dash_table.DataTable(
        id=idx,
        style_cell={'font-family': 'Montserrat'},
        style_data_conditional=[
            {
                'if': {'column_id': 'intitule'},
                'textAlign': 'left'
            }] + [
            {
                'if': {'row_index': 'odd'},
                'backgroundColor': 'rgb(248, 248, 248)'
            }
        ],
        style_header={
            'backgroundColor': 'rgb(230, 230, 230)',
            'fontWeight': 'bold'
        }
    )

