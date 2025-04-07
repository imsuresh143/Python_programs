Number=int(input("Enter the value for x(where x>>2)"))
x=0
y=2
count=2
if Number<=0:
    print("pls enter the positive integer")
elif Number==1:
    print("fibonacci sequence is") 
    print(x)
else:
    print("fibonacci sequence is")
    print(x," ",y)
    while count<Number:
        z=x+y
        print(z)
        x=y
        y=z
        count+1
               
