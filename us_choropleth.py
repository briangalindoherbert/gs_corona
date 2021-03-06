# encoding=utf-8

import pandas as pd
import plotly.express as px

# BEGIN Variable Definition
MAPS_IMAGE_FORMATS = {'png8', 'png', 'png32', 'gif', 'jpg', 'jpg-baseline'}
MAPS_MAP_TYPES = {'roadmap', 'satellite', 'terrain', 'hybrid'}

# END Variable Definition

class StaticMapMarker(StaticMapParam):
    """Handles marker parameters for Maps Static API."""

    def __init__(self, locations,
                 size=None, color=None, label=None):
        """
        :param locations: Specifies the locations of the markers on
            the map.
        :type locations: list

        :param size: Specifies the size of the marker.
        :type size: str

        :param color: Specifies a color of the marker.
        :type color: str

        :param label: Specifies a single uppercase alphanumeric
            character to be displaied on marker.
        :type label: str
        """

        super(StaticMapMarker, self).__init__()

        if size:
            self.params.append("size:%s" % size)

        if color:
            self.params.append("color:%s" % color)

        if label:
            if len(label) != 1 or not label.isupper() or not label.isalnum():
                raise ValueError("Invalid label")
            self.params.append("label:%s" % label)

        self.params.append(convert.location_list(locations))

ef static_map(client, size,
               center=None, zoom=None, scale=None,
               format=None, maptype=None, language=None, region=None,
               markers=None, path=None, visible=None, style=None):
    """
    Downloads a map image from the Maps Static API.

    See https://developers.google.com/maps/documentation/maps-static/intro
    for more info, including more detail for each parameter below.

    :param size: Defines the rectangular dimensions of the map image.
    :type param: int or list

    :param center: Defines the center of the map, equidistant from all edges
        of the map.
    :type center: dict or list or string

    :param zoom: Defines the zoom level of the map, which determines the
        magnification level of the map.
    :type zoom: int

    :param scale: Affects the number of pixels that are returned.
    :type scale: int

    :param format: Defines the format of the resulting image.
    :type format: string

    :param maptype: defines the type of map to construct. There are several
        possible maptype values, including roadmap, satellite, hybrid,
        and terrain.
    :type maptype: string

    :param language: defines the language to use for display of labels on
        map tiles.
    :type language: string

    :param region: defines the appropriate borders to display, based on
        geo-political sensitivities.
    :type region: string

    :param markers: define one or more markers to attach to the image at
        specified locations.
    :type markers: StaticMapMarker

    :param path: defines a single path of two or more connected points to
        overlay on the image at specified locations.
    :type path: StaticMapPath

    :param visible: specifies one or more locations that should remain visible
        on the map, though no markers or other indicators will be displayed.
    :type visible: list of dict

    :param style: defines a custom style to alter the presentation of
        a specific feature (roads, parks, and other features) of the map.
    :type style: list of dict

    :rtype: iterator containing the raw image data, which typically can be
        used to save an image file locally. For example:

        ```
        f = open(local_filename, 'wb')
        for chunk in client.static_map(size=(400, 400),
                                       center=(52.520103, 13.404871),
                                       zoom=15):
            if chunk:
                f.write(chunk)
        f.close()
        ```
    """

    params = {"size": convert.size(size)}

    if not markers:
        if not (center or zoom is not None):
            raise ValueError(
                "both center and zoom are required"
                "when markers is not specifed"
            )

    if center:
        params["center"] = convert.latlng(center)

    if zoom is not None:
        params["zoom"] = zoom

    if scale is not None:
        params["scale"] = scale

    if format:
        if format not in MAPS_IMAGE_FORMATS:
             raise ValueError("Invalid image format")
        params['format'] = format

    if maptype:
        if maptype not in MAPS_MAP_TYPES:
            raise ValueError("Invalid maptype")
        params["maptype"] = maptype

    if language:
        params["language"] = language

    if region:
        params["region"] = region

    if markers:
        params["markers"] = markers

    if path:
        params["path"] = path

    if visible:
        params["visible"] = convert.location_list(visible)

    if style:
        params["style"] = convert.components(style)

    response = client._request(
        "/maps/api/staticmap",
        params,
        extract_body=lambda response: response,
        requests_kwargs={"stream": True},
    )
    return response.iter_content()

def do_choro(pdf: pd.DataFrame):
    data = [ dict(
            type='choropleth',
            colorscale = scl,
            autocolorscale = False,
            locations = df['code'],
            z = df['total exports'].astype(float),
            locationmode = 'USA-states',
            text = df['text'],
            marker = dict(
                line = dict (
                    color = 'rgb(255,255,255)',
                    width = 2
                ) ),
            colorbar = dict(
                title = "Millions USD")
            ) ]
    fig = px.scatter_mapbox(us_cities, lat="lat", lon="lon", hover_name="City", hover_data=["State", "Population"],
                            color_discrete_sequence=["fuchsia"], zoom=3, height=300)
    fig.update_layout(mapbox_style="open-street-map")
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    fig.show()
    fig = dict( data=data, layout=layout )
    py.iplot( fig, filename='d3-cloropleth-map' )
    return fig
