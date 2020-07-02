## Google Maps API Params ##
center - 

**zoom** - int from 0 to 21
    1: world
    5: continent
    10: city
    15: streets
    20: buildings
    
size - width by height in pixels
    ex: 600x400

scale - multiplier for *size* parm
    useful to improve res on mobile
    
format - allowed values:
    png8 or png (default) specifies the 8-bit PNG format.
    png32 specifies the 32-bit PNG format.
    gif specifies the GIF format.
    jpg specifies the JPEG compression format.
    jpg-baseline non-progressive compression format

maptype - 
    roadmap (default) specifies a standard roadmap image, as is normally shown on the Google Maps website. If no maptype value is specified, the Maps Static API serves roadmap tiles by default.
    satellite specifies a satellite image.
    terrain specifies a physical relief map image, showing terrain and vegetation.
    hybrid specifies a hybrid of the satellite and roadmap image,

markers - formatted as:
    markerStyles|markerLocation1| markerLocation2
    Styles:  color:blue
            size: {tiny, mid, small}
            label: {A-Z, 0-9}

visible=

key=

signature=
