a = 2 * 6 - 2   
for b in range(6, -1, -1):    
    for c in range(a, 0, -1):  
        print(end=" ")  
    a = a + 1   
    for c in range(0, b + 1):  
        print("*", end=" ")  
    print("")