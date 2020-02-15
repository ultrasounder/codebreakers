"""APply the formula fib(n-1) + fib(n-2)"""

# def nfib(n):
#     if n == 2:
#         return 1
#     elif n == 1:
#         return 0
#     else:
#         return nfib(n-1) + nfib(n-2)

# print(nfib(6))
# #time complexity is 2^n as at each nfib we are calling two operations

# using memoization O(n) time and o(n) space
def nfib(n, memoize = {1:0, 2:1}):
    if n in memoize:
        return memoize[n]
    else:
        memoize[n] = nfib(n-1, memoize) + nfib(n -2, memoize)
        return memoize[n]

