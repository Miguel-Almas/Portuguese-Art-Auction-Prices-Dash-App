import dash
import dash_bootstrap_components as dbc

# bootstrap theme
# https://bootswatch.com/lux/
external_stylesheets = [dbc.themes.LUX]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets,    
	meta_tags=[{"name": "HandheldFriendly", "content": "true"},
                {"name": "viewport", "content": "width=device-width,initial-scale=1.0,minimum-scale=0.5, maximum-scale=1.0, user-scalable=yes"},])

server = app.server
app.config.suppress_callback_exceptions = True