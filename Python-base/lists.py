# Access list items

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])


# Change list items

thislists = ["apple", "banana", "cherry"]
thislists[1] = "blackcurrant"
print(thislists)

# delete list items 

list = ["apple", "banana", "cherry"]
del list[0]
print(list)

lists = ["apple", "banana", "cherry"]
lists.pop()
print(lists)

# loop lists

for x in thislist:
  print(x)

# List comprehension

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "e" in x]

print(newlist)

# join lists

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)