from weather_data import WeatherData

class WeatherDisplay(object):
  """a sample object that pretends to hold weather data"""
  def update(self): pass

class OurWeatherData(WeatherData):
  """build our weather data class on the vendor-supplied one"""

  def __init__(self):
    self.current_conditions_display = WeatherDisplay()
    self.statistics_display = WeatherDisplay()
    self.forecast_display = WeatherDisplay()

  def measurements_changed(self):
    temp = self.get_temp()
    humidity = self.get_humidity()
    pressure = self.get_pressure()
    self.current_conditions_display.update(temp, humidity, pressure)
    self.statistics_display.update(temp, humidity, pressure)
    self.forecast_display.update(temp, humidity, pressure)

