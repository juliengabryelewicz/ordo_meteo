import requests
import json
import math

from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.screenmanager import Screen
from kivy.storage.jsonstore import JsonStore
from kivy.logger import Logger
from kivy.clock import Clock
from kivy_garden.mapview import MapView, MapMarker
from kivy.uix.image import AsyncImage

class MeteoScreen(Screen):
	city_meteo = StringProperty("")
	min_temperature = StringProperty("")
	max_temperature = StringProperty("")
	description = StringProperty("")
	mapview = ObjectProperty(None)
	icon_meteo= ObjectProperty(None)

	def __init__(self, **kwargs):
		super(MeteoScreen, self).__init__(**kwargs)

	def on_enter(self, *args):
		self.store = JsonStore("parameters/meteo.json")
		self.api_key = self.store.get("openweather_api_key")
		self.city = self.store.get("openweather_api_city")
		self.url_weather = "https://api.openweathermap.org/data/2.5/weather?q="+self.city+"&appid="+self.api_key
		Clock.schedule_once(self.get_details)
	
	def get_details(self,dt):
		self.mapview.clear_widgets()
		self.icon_meteo.clear_widgets()
		response = requests.get(self.url_weather)
		data = json.loads(response.text)
		self.city_meteo = data["name"]
		self.min_temperature = "Min: "+str(math.floor(data["main"]["temp_min"] - 273.15))+" °C"
		self.max_temperature = "Max: "+str(math.floor(data["main"]["temp_max"] - 273.15))+" °C"
		self.description = data["weather"][0]["description"]
		mapview = MapView(zoom=11, lat=data["coord"]["lat"], lon=data["coord"]["lon"])
		marker = MapMarker(lon=data["coord"]["lon"], lat=data["coord"]["lat"])
		mapview.add_marker(marker)
		self.mapview.add_widget(mapview)
		aimg = AsyncImage(source='https://openweathermap.org/img/wn/'+data["weather"][0]["icon"]+'@2x.png')
		self.icon_meteo.add_widget(aimg)
