# local scope

def Myfunc():
    x=200
    print(x)

Myfunc()

# inside function

def Myfuncs():
    x=300
    def Myinnerfunc():
        print(x)
    Myinnerfunc()
Myfuncs()

# global scope

x=100

def Myfunc():
    print(x)

Myfunc()
print(x)

# Naming Variables

# x=100

def Myfunc():
    x=200
    print(x)

Myfunc()
print(x)

# Global Keyword

x=400
def Myfunc():
    global x
    x=300

Myfunc()
print(x)