# class & objects

class MyClass:
    x=4

p1 =MyClass()

print(p1.x)

#  the__init__() Function


class persons:
  def __init__(self, name, age):
    self.name = name 
    self.age = age
    
p1 = persons("sham", 33) 

print(p1)

# The __str__() Function


class Persons:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

p2 = Persons("John", 36)

print(p2)



# The self Parameter


class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()