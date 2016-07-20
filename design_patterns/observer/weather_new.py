from abc import ABCMeta, abstractmethod
from weather_data import WeatherData

# observer pattern generic classes

class Subject(object):
  @abstractmethod
  def register_observer(self, o): pass
  @abstractmethod
  def remove_observer(self, o): pass
  @abstractmethod
  def notify_observer(self): pass

class Observer(object):
  def update(self, temp, humidity, pressure): pass

# core classes

class WeatherDisplay(object):
  """a sample object that pretends to hold weather data"""
  def update(self): pass

class OurWeatherData(WeatherData, Subject):
  """build our weather data class on the vendor-supplied one"""

  def __init__(self):
    self.observers = []

  def register_observer(self, o):
    self.observers.append(o)

  def remove_observer(self, o):
    self.observers.remove(o)

  def notify_observers(self):
    for o in self.observers:
      o.update(self.temp, self.humidity, self.pressure)

  def measurements_changed(self):
    self.notify_observers()

  def set_measurements(self, temp, humidity, pressure):
    """since we don't have a real weather station, use this function to test"""
    self.temp = temp
    self.humidity = humidity
    self.pressure = pressure
    self.measurements_changed()

class CurrentCondition(object):
  """an obsserver (object)"""

  def __init__(self, weather_data):
    self.weather_data = weather_data
    weather_data.register_observer(self)
    temp = 0
    humidity = 0

  def update(self, temp, humidity, display):
    self.temp = temp
    self.humidity = humidity
    self.display()

  def display(self):
    print "Current condition: %.1fF degrees and %.1f%% humidity" % (self.temp, self.humidity)

# testing

if __name__ == '__main__':

  weather_station = OurWeatherData()

  current_conditions_display = CurrentCondition(weather_station)
  statistics_display = CurrentCondition(weather_station)
  forecast_display = CurrentCondition(weather_station)

  weather_station.set_measurements(80, 65, 30.4)
  print
  weather_station.set_measurements(82, 70, 29.2)
  print
  weather_station.remove_observer(statistics_display)
  weather_station.set_measurements(78, 95, 29.2)

