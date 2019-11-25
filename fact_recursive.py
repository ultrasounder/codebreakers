def fact_recursive(n):
    if n == 0:
        return 1
    else:
        return n * fact_recursive(n-1)
    
print(fact_recursive(3))
    
    