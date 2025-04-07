#construct a function perfect_square(number)  that return a number otherwise its returns -1
import math
def prefect_square(number):
    square_root= math.isqrt(number)
    if square_root*square_root==number:
        return number
    else:
        return -1
print(prefect_square(1))    
print(prefect_square(144))
