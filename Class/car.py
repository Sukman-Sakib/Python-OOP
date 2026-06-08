class Car:
  def display(self, brand, model):
    self.brand = brand
    self.model = model

car1 = Car()
car1.display("Merc", "Petronas")
print(car1.brand)
print(car1.model)