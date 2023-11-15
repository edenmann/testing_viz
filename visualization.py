import plotly.graph_objects as go

import pandas as pd

df = pd.read_csv('https://github.com/marestaing/hosting/blob/main/visited_states.csv?raw=true')

fig = go.Figure(data=go.Choropleth(
    locations=df['code'], # Spatial coordinates
    z = df['number students'].astype(float), # Data to be color-coded
    locationmode = 'USA-states', # set of locations match entries in `locations`
    colorscale = 'plasma',
    colorbar_title = "Visit Frequency: Cold to Hot",
))

fig.update_layout(
    title_text = 'States Visited by Students',
    geo_scope='usa', # limit map scope to USA
)

fig.show()