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

# from math import sqrt

# def is_prime(n):
#     """Determines the primality of a given value.
#     n an integer to test for primality.
#     returns true if n is prime. Otherwise returns false."""

#     root = round(sqrt(n)) + 1

#     #Try all potential factors from 2 to the square root of n
#     for trial_factor in range(2, root):
#         if n % trial_factor == 0:
#             return False
#         return True

# def main():
#     """
#     Tests for primality each integer from 2 up to a value provided by the user.
#     If an integer is a prime, it prints out.otherwise the number is nor printed."""

#     max_value = int(input("Display primes upto this number:"))

#     for value in range(2, max_value + 1):
#         if is_prime(value):
#             print(value, end = ' ')
#     print()

# main()

from random import randrange

def show_die(spots):
    """Draw a picture of a die with number of spots indicated.
    spots is the same number of spots on the face.
    """

    print("+------+")
    if spots == 1:
        print("|      |")
        print("|   *  |")
        print("|      |")
    elif spots == 2:
        print("|*     |")
        print("|      |")
        print("|     *|")
    elif spots == 3:
        print("|     *|")
        print("|   *  |")
        print("|*     |")
    elif spots == 4:
        print("|*    *|")
        print("|      |")
        print("|*    *|")
    elif spots == 5:
        print("| *   * |")
        print("|   *   |")
        print("|*     *|")
    elif spots == 6:
        print("| * * * |")
        print("|       |")
        print("|*  * * |")
    else:
        print("*** Error: illegal die value:")

def roll():
    """returns a pseudorandom number in the range 1 ....6, inclusive"""
    return randrange(1, 7)

def main():
    """simulates the roll """

    for i in range(0, 3):
        show_die(roll())
main()




