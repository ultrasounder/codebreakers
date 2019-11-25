def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(40))

#fibonacci cached version

previous = {0 :0, 1: 1}
def fibonacci(n):
    if previous.has_key(n):
        return previous[n]
    else:
        new_value = fibonacci(n-1) + fibonacci(n-2)
        previous[n] = new_value
        return new_value
fibonacci(100)