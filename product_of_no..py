# given 2 integer number, return thir product 
# the product is equal to or lower than 10

def product(num1,num2):
    product=num1*num2
    if product<=10:
        return product
    else:
        return"The product is greater than 10"
x=product(2,3)
print(x)
x=product(5,3)
print(x)
