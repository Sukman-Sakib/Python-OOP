from datetime import datetime

class User:
  def __init__(self, username, email, password):
    self.username = username
    self._email = email
    self.password =  password

  def get_email(self):
    print(f"Email Accessed at {datetime.now()}")
    return self._email
  
  def set_email(self, new_email):
    if "@" in new_email and ".com" in new_email:
      self._email = new_email
    else: 
      print("Invalid Email it is")


user = User("Sakib", "Sakib@gmail.com", "123456")
#print(user.get_email())

user.set_email("rafi@outlook.com")
print(user.get_email())

