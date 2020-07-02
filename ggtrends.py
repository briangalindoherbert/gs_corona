# encoding=utf-8
""" I'm testing ggplot's ability to support some choropleths I want to build
"""

import os
import pandas as pd
from matplotlib.pyplot import *
import plotly.graph_objects as go
from plotly.graph_objects import Layout
from plotly.io import renderers
# from shapely.geometry import Point, Polygon

SHAPE_RESTORE_SHX= 'YES'
shapef = 'cb_2019_us_state_5m.shp'
shapedir = 'maps'
fq_shp = os.path.join(shapedir, shapef)

data: dict(str, any) = {
    type: 'choropleth',
    locations: ['GA','AZ', 'WI'],
    locationmode:'USA-states',
    colorscale: ['Viridis'],
    z: [10,20,30]
}
layt: dict = {}

layt = dict(geo=dict(scope='usa'))
map = go.Figure(data=[data], layout = layout)
py.offline.plot(map)

Layout.template

