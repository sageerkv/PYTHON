#  Functions

def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(12)


# Lambda


def myfunc(n):
  return lambda a : a * n

print("\n\nlambda Example Results")
mydoubler = myfunc(2)
mytripler = myfunc(4)

print(mydoubler(11))
print(mytripler(11))