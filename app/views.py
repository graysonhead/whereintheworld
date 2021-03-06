from app import app, aprs
from flask import render_template
from flask_googlemaps import Map, icons
import time
import config

@app.route('/', methods=['GET'])
def homepage():
	loc = aprs.location()
	loc['entries'][0]['lasttime'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(loc['entries'][0]['lasttime'])))
	mymap = Map(
		identifier="view-side",
		lat=float(loc['entries'][0]['lat']),
		lng=float(loc['entries'][0]['lng']),
		markers=[(float(loc['entries'][0]['lat']), float(loc['entries'][0]['lng']))],
		style="height:400px;width:100%;margin:0",
		maptype='HYBRID'
	)
	return render_template(
		'index.html',
		name=config.name,
		loc=loc,
		cloc_map=mymap
	)