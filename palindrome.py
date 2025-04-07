def palindrome(number):
    num=number
    rev=num[::-1]
    if rev==num:
        return 1
    else:
        return 0

number=int(input("enter the number checked"))
if palindrome(number):
    print("number is palindrome")
else:
    print("number is not palindrome")   
    
