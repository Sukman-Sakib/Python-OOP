class Student:
  def __init__(self, name, grade):
    self.name = name
    self.grade = grade

  @property
  def grade(self):
    return self._grade
  
  @grade.setter
  def grade(self, grade):
    if(grade<100 and grade>0):
      self._grade = grade
    else:
      self._grade = None
      
     
  @property
  def result(self):
    if self._grade is None:
      return "No Valid"
    elif (self._grade>=80):
      return "A+"
    elif (self._grade>=70):
      return "A"
    elif (self._grade>=60):
       return "A-"
    elif(self._grade>=50):
       return "B"
    else:
      return "Fail"


   
s = Student("Rafi", 135)
print(s.result)