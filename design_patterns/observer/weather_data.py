from abc import abstractmethod

class WeatherData(object):
  """a vendor-supplied weather class. it will call the measurements_changed when appropriate"""
  def get_temperature(self): pass
  def get_humidity(self): pass
  def get_pressure(self): pass

  @abstractmethod
  def measurements_changed(self): pass

