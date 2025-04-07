def count1(s):
    vowels="AEIOUaeiou"
    count=0
    for i in s:
        if i in vowels:
            count+=1
    return count
print(count1("python"))
