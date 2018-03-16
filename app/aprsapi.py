import requests
import config

class AprsFI:
	apikey = None
	callsign = None

	def __init__(self, apikey=None, callsign=None):
		self.apikey = apikey
		self.callsign = callsign

	def location(self):
		params = {
			'name': self.callsign,
			'what': 'loc',
			'apikey': self.apikey,
			'format': 'json'
		}
		try:
			r = requests.get(config.aprsfi_url + 'api/get', params=params)
			r.raise_for_status()
			return r.json()
		except:
			raise