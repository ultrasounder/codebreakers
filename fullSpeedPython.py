#list excercises
# using list comprehensions create a list with squares of the first 10 numbers

square = [x * x for x in range(0,10)]
print(square)

#create a list comprehension with cubes of first 20 numbers

cubes = [x * x * x for x in range(0,20)]
print(cubes)

#Create a list comprehension with all the even numbers from 0 to 20, and another one with all the odd numbers.

even = [ x for x in range(0,20) if x % 2 == 0]
print(even)

odd = [ x for x in range(0,20) if x % 2 !=0]
print(odd)

#Create a list comprehension with all the even numbers from 0 to 20, and another one with all the odd numbers.

# Create a list with the squares of the even numbers from 0 to 20, and sum the list
# using the “sum” function. The result should be 1140. First create the list using list
# comprehensions, check the result, then apply the sum to the list comprehension.

SumOfSquares = [ sum(x * x  for x in range(0,20) if x % 2 == 0)]
print(SumOfSquares)

# Make a list comprehension that returns a list with the squares of all even numbers
# from 0 to 20, but ignore those numbers that are divisible by 3. In other words,
# each number should be divisible by 2 and not divisible by 3. Search for the “and”
# keyword in the Python documentation. The resulting list is [4, 16, 64, 100, 196,
# 256].

SquaresEven = [x * x for x in range(0,20) if (x % 2 == 0) and (x % 3 != 0)]
print(SquaresEven)

