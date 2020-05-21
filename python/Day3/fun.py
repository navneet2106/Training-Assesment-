class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name , self.age)

p1 = Person("Navneet", 24)
p1.myfunc()