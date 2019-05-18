# core
from core import settings
# core modules / packages
from core.modules import tts
from core.packages import weather

"""
weather
says the todays'
weather
"""
def ex(cmd):
    # check the weather for the set location
    weather_text = weather.Weather.lookup(settings.LOCATION)

    tts.say(weather_text)
