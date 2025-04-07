def triangle(T):
    for i in range(1,T+1):
        for j in range(i):
            print("*",end="")
        print()
T=int(input("enter the number of row"))
triangle(T)            
