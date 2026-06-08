class Student:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def show_info(self):
    print(f"Name: {self.name}\n Age: {self.age}")

s1 = Student("Rafi", 22)
s1.show_info()