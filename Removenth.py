#removenth("MANGO"1)return MNGO
#removenth("MANGO"3)return MANO

def removenth(s,n):
    if n>=len(s):
        return s
    else:
        return s[ :n]+s[n+1: ]
print(removenth("MANGO",1))
print(removenth("MANGO",3))    




def removenth(s,n):
    if n>=len(s):
        return s
    else:
        return s[ :n]+s[n+1: ]
print(removenth("MANGO",4))
print(removenth("MANGO",2))    
print(removenth("MANGO",5))  
