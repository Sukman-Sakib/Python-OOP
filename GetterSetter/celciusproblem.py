class Temperature:
  def __init__(self, temp):
    self._temp = temp
  
  @property
  def celcius(self):
    return self._temp
  
  @celcius.setter
  def celcius(self, new_temp):
    if (new_temp)>-273.15:
      self._temp = new_temp

  @property
  def fahrennheit(self):
    return (self._temp*9/5)+32
  
  

user = Temperature(34)
print(user.celcius)
user.celcius = 25
print(user.celcius)
print(user.fahrennheit)