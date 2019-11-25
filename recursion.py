def mult_iter(a,b):
    result = 0
    while b > 0:
        result += a
        b -= 1
    return result

print(mult_iter(3,4))

def mult(a,b):
    result = 0
    if b == 1:
        return a
    else:
        result = a + mult(a,b-1)
    
    return result
print(mult(3,4))