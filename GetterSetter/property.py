class User:
  def __init__(self, username, email, password):
    self.username = username
    self.email =  email
    self._password = password
   
  @property
  def password(self):
    print("Accessed")
    return self._password
    
  @password.setter
  def password(self, new_password):
    if len(new_password)>6:
      self._password = new_password
      print("Password Accessed") 
    else: 
      print("Invalid Password")


user =  User("Sakib", "sakib@gmail.com", "suptman2230989")
user.password = "324"
print(user.password)
