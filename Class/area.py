class Rectangle:
  def __init__(self, length, width):
    self.length = length
    self.width = width
  def area(self):
    return f"The Area is {self.length*self.width}"
  def perimeter(self):
    return f"The Perimeter is {(2*self.length)+(2*self.width)}"

rec = Rectangle(10, 5)
print(rec.area())
print(rec.perimeter())
