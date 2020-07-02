# gs_corona
GalindoSoft app to acquire, wrangle and present covid-19 data for U.S./States tests-cases-hospitalizations-deaths, including plots and choropleths.

Data sources include git repositories from Johns Hopkins, the covidtrackingproject, New York Times, the CDC Wonder database, and directly from State Departments of Health.

Currently I am using Plotly, mainly plotly.graph_objects (low level interface, finer grained control than express) and plot-geo (choropleths). Most of my prior plotting work has been with matplotlib or simply pandas extensions, so this part of code likely to change more as I climb plotly learning curve!

fyi, I'm developing and testing this app on machine with Python 3.8.

I am also using Google Maps API (I am doing some parellel work to test/compare Google approach with plotly-geo for my choropleths). I need to make sure I have all necessary copyrights displayed (#TODO). Google Maps API use requires a billing account with Google and registration for an API key. I am excluding including the file with the API key for obvious reasons- if you want to clone and use this you just need to insert your own file with your key.
