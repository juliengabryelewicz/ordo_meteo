import plugin
from .screens.meteo_screen import MeteoScreen

class MeteoPlugin(plugin.PluginObject):

	def get_main_screen():
		return MeteoScreen()

	def get_screens():
		return [MeteoScreen()]