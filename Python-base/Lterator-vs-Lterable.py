# iter,next

mytuple =("tiger", "cat", "dog")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

mytuple =("tiger")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

# Looping

mytuple = ("apple", "banana", "cherry")

for x in mytuple:
 print(x)

mytuple = ("apple")

for y in mytuple:
 print(y)

#Create an Iterator

class MyNumber:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        x = self.a
        self.a += 1
        return x
MyClass = MyNumber()
Myiter = iter(MyClass)

print(next(Myiter))
print(next(Myiter))
print(next(Myiter))
print(next(Myiter))
print(next(Myiter))
print(next(Myiter))
print(next(Myiter))

# StopIteration

class MyNumbers:
    def __iter__(self):
        self.a  = 1
        return self

    def __next__(self):
     if self.a <= 20:
        x = self.a
        self.a += 1
        return x
     else:
        raise StopIteration

MyClass = MyNumbers()
Myiter = iter(MyClass)

for x in Myiter:
    print(x)    
