# encoding=utf-8

import pandas as pd
import plotly.io as pio
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from datetime import datetime

pio.renderers.default = "png"  # can also be set to browser

def getelapsed(pdin: pd.DataFrame, startdt):
	""" takes a series of date strings and returns the number of elapsed days
    from the earliest to the last date
    """
	dmax = pdin.date.max()
	dmin = datetime.strptime(startdt, '%Y-%m-%d')
	ddif: datetime.timedelta = dmax - dmin
	return ddif.days

def get_gadaily(fnam: str):
	""" get_gadaily reads the comprehensive times series covid file for Georgia
	"""
	gadf = pd.read_csv(fnam, header=0, parse_dates=True)
	gadf.date = pd.to_datetime(gadf.date, format='%Y%m%d', errors='ignore')
	gadf.set_index('date', drop=False)
	gadf.sort_index()
	gadf['seq'] = None
	scol: int = gadf.columns.get_loc('seq')
	poscol: int = gadf.columns.get_loc('dailyPosRate')
	seqx: int = len(gadf)
	for i in range(0, len(gadf)):
		gadf.iloc[i, scol] = seqx - i
		gadf.iat[i, poscol] = str(gadf.iat[i, poscol]).strip("%")
	gadf.dailyPosRate = gadf.dailyPosRate.astype('float32')
	return gadf

def do_plotly(pdc: pd.DataFrame):
	""" doplotly takes a pd dataframe and parses and passes it to graph using
	plotly.  Note: plotly scatter requires a dict
	:param pdc: the DataFrame used by plotly
	:param option: a string controlling output
	:return: DataFrame for one state
	"""
	xrange = getelapsed(pdc, '2020-06-03')
	dfmod = pdc.loc[pdc.date >= '2020-06-03']
	scol: int = dfmod.columns.get_loc('seq')
	for i in range(0, len(dfmod)):
		dfmod.iat[i, scol] = xrange - i
	xx: list = dfmod.seq.array
	yy = dfmod['dailyPosRate'].array
	typedict: dict = {"type": "scatter"}
	layoutdict: dict = {"title": "Daily COVID-19 Viral Testing: Georgia"}
	#	fig = go.Figure(typedict)
	fig = make_subplots(specs=[[{"secondary_y": True}]])

	ylbl = 'percent of daily tests that are positive for Virus'
	y2lbl = 'number of daily COVID-19 Viral tests'
	xlbl = str(xrange) + " elapsed days starting June 03, 2020"

	fig.add_trace(go.Scatter(x=xx, y=yy, line=dict(color='firebrick', width=2), \
		mode='markers', name='% Positive Tests', text=dfmod.date), secondary_y=False)
	yy = dfmod.dailyPosRate.rolling(window=3).mean()
	fig.add_trace(go.Scatter(x=xx, y=yy, line=dict(color='darkgreen', width=2), \
		name='3-day avg PosRate'), secondary_y=False)

	fig.add_trace(go.Scatter(x=xx, y=dfmod.dResults.array , line= \
		dict(color='darkblue', width=1), mode='markers', name='% Positive Tests', \
		text=dfmod.dResults.array), secondary_y=True,)
	yy = dfmod.dResults.rolling(window=3).mean()
	fig.add_trace(go.Scatter(x=xx, y=yy, line=dict(color='darkblue', width=1), \
		name='3-day avg Tests'), secondary_y=True)

	titlex: str = 'Georgia COVID-19 Daily Total Tests vs. Positive Rate'
	fig.update_layout(title=layoutdict['title'], xaxis_title=xlbl)
	fig.update_yaxes(title_text=ylbl, secondary_y=False)
	fig.update_yaxes(title_text=y2lbl, secondary_y=True)

	fig.show()
	return 0
