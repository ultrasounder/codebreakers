# 

# def factorial(n):
#     if n == 0 or n == 1: # base case
#         return 1
    
#     return factorial(n-1) * n # reduction step
# print(factorial(4))

def fib(n):
    if n == 0 or n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)
print(fib(6))