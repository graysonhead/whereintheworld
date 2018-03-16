from flask import Flask
from flask_googlemaps import GoogleMaps
import config
from .aprsapi import *

aprs = AprsFI(apikey=config.aprsfi_api_key, callsign='kg5puw-9')
app = Flask(__name__, static_folder='static', static_url_path='')
GoogleMaps(app, key=config.google_maps_apikey)

from app import views