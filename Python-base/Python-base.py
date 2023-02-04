# print variable,type of variable

print("hello world")
print(10)
print(10+10)
print(10j)
a=3
b="mango"
c=10j
d=3.14
e=True
f=False
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(a))
print(type(e))
print(type(f))

# arithematic operators

a=5
b=2
c=a+b
c=a-b
c=a*b
c=a/b
c=a%b
c=a//b
print(c)

# assignment operators

a=5
a+=5
a-=5
a*=5
a/=5
a%=5
a//=5
b=a**2
a**=2
print(a)
print(b)

# comparison operators

a=5
print(a==5)
print(a<=5)
print(a>=6)
print(a!=5)


# logical operators

a=5
and
print((a==5) & (a<=5))
print((a==5) & (a!=5))

or
print((a==5) | (a!=5))
print((a!=5) | (a!=5))

not
print(not(a<5))

# python casting

x=int(3.14)
y=str(2)
z=float(4)
print(x)
print(y)
print(type(y))
print(z)

# python strings

x="this is"
y="paragraph"
z=x+y
a=x+" "+y
print(x[2:6])
print(len(x))
s="        this is"
t="THIS IS"
print(s)
print(s.strip())
print(s.upper())
print(t.lower())
print(x.replace("this","they"))
name="john"
age=35
z="this is {} and he is {} years old"
print(z.format(name,age))