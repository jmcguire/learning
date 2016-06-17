from weather_data import WeatherData

class WeatherDisplay(object):
  """a sample object that pretends to hold weather data"""
  def update(self): pass

class OurWeatherData(WeatherData):
  """build our weather data class on the vendor-supplied one"""

  def __init__(self):
    current_conditions_display = WeatherDisplay()
    statistics_display = WeatherDisplay()
    forecast_display = WeatherDisplay()
  
  def measurements_changed(self):
    temp = self.get_temp()
    humidity = self.get_humidity()
    pressure = self.get_pressure()
    current_conditions_display.update(temp, humidity, pressure)
    statistics_display.update(temp, humidity, pressure)
    forecast_display.update(temp, humidity, pressure)

