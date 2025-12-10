import sys

def mysterious_function(x, y:int) -> int:
    a = 0
    for i in x:
        if i > y :
            a += i
    return a / len(x)
    return 1


