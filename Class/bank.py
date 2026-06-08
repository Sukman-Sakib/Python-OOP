class BankAccount:
  def __init__(self, owner, balance):
    self.owner = owner
    self.balance = balance

  def deposit(self, amount):
   self.balance+=amount
  
  def withdraw(self, amount):
    self.balance-=amount
  
  def show_balance(self):
    return self.balance

acc = BankAccount("Rafi", 1200)
acc.deposit(1200)
acc.withdraw(500)
print(acc.show_balance())