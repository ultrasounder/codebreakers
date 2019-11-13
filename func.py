# def count_to_10():
#     for i in range(1, 11):
#         print(i, end = ' ')

#     print()


# print("Going to coun to ten:")

# count_to_10()


# def count_to_n(n):
#     for i in range(1, n +1):
#         print(i, end = ' ')
#     print()
# count_to_n(100)


# def count_to_n(n):
#     for i in range(1, n+1):
#         print(i, end = ' ')
#     print()

# for i in range(1,10):
#     count_to_n(i)

from math import sqrt

def is_prime(n):
    """Determines the primality of a given value.
    n an integer to test for primality.
    returns true if n is prime. Otherwise returns false."""

    root = round(sqrt(n)) + 1

    #Try all potential factors from 2 to the square root of n
    for trial_factor in range(2, root):
        if n % trial_factor == 0:
            return False
        return True

def main():
    """
    Tests for primality each integer from 2 up to a value provided by the user.
    If an integer is a prime, it prints out.otherwise the number is nor printed."""

    max_value = int(input("Display primes upto this number:"))

    for value in range(2, max_value + 1):
        if is_prime(value):
            print(value, end = ' ')
    print()

main()