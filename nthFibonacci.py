"""APply the formula fib(n-1) + fib(n-2)"""

def nfib(n):
    if n == 2:
        return 1
    elif n == 1:
        return 0
    else:
        return nfib(n-1) + nfib(n-2)

print(nfib(6))