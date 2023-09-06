from check import check_install
from plugin import find_required_plugin
import os

check_install(set(find_required_plugin(os.path.dirname(os.path.realpath(__file__))).split(",")))

from .ordo_meteo import MeteoPlugin