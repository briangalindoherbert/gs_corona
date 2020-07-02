# encoding=utf-8
""" gmap2020 is a basic interface to the google maps api staticmap, my plan
is this functionality will be the framework to enhance other gssoft apps, such
as simplecovid, with gis visualization.
NOTE:  need to modify to encrypt the api key so that it is not simply sent
in the clear with each http get or post.
"""

import pandas as pd
import googlemaps
import requests
import os
from  plotly.io import renderers
from trends import *

pd.set_option('display.precision', 6)
pd.set_option('display.date_yearfirst', True)
# pd.set_option('plotting.backend', )
renderers.default = 'browser'

datadir: str = 'rawdata'
fgadaily: str = os.path.join(datadir, "covtrackingGAdaily.csv")
fkey: str = "api.csv"

MAP_URL = 'https://maps.googleapis.com/maps/api/staticmap?'
with open(fkey, 'r') as filehdl:
    fcontent = filehdl.readlines()
    for line in fcontent:
        if len(line) >= 8:
            MAPS_API = line
KEYVAL = 'size=600x600&maptype=roadmap'
GPARM: dict = {'center': 'Kansas City, MO',
            'zoom': '4',
            'size': '600x300',
            'scale': '1',
            'format': 'png32',
            'maptype': 'roadmap',
            'markers': '',
            'visible': '',
            'key': MAPS_API
}

URLPARMS = MAP_URL + "center=" + GPARM['center'] + "&zoom=" + GPARM['zoom'] \
           + "&maptype=" + GPARM['maptype'] + "&size=" + GPARM['size'] + \
           "&scale=" + GPARM['scale'] + "&key=" + MAPS_API

# gmaps = googlemaps.Client(key=MAPS_API)
# geocode_result = gmaps.geocode('Saint Louis, MO')
# Look up address with reverse geocoding
# reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))

def get_static(encoded: str):
    r = requests.get(encoded)
    with open('./img/gmap_us.png', 'wb') as file:
        file.write(r.content)
    file.close()
    return 0

# get_static(URLPARMS)
ga_daily: pd.DataFrame = get_gadaily(fgadaily)
do_plotly(ga_daily)

