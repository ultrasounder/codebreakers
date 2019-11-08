#Section one Basic review of the List and its Python built-ins Zip, Enumerate, 

my_list = [] # create an empty list
print(type(my_list))
my_list.append(1)#append takes O(1)
print(my_list)

for i in range(0,6):
    my_list.append(i)
print(my_list)

#You can pop from the end of the list in O(1)
last_element = my_list.pop()
print(last_element)
print(my_list)

first_element = my_list.pop(0)# this is O(n) worst case
print(first_element)
print(my_list)
print(my_list[2])#const time index access

print(3 in my_list)#Check whether an element in a list is O(n)
print(200 in my_list)

#iterating through a list is O(n)
total_sum = 0
for num in my_list:
    total_sum += num
print(total_sum)

#we can create a new list using the existing list with what we call list comprehension
string_numbers = [str(x) for x in my_list]
print(string_numbers)

even_numbers = [x for x in my_list if(x % 2) == 0]
print(even_numbers)

#zip    
names = ["sam", "Bob", "Ann"]
ages = [10, 8, 13]

#zip combines two parallel lists into a list of tuples
names_and_ages = zip(names, ages)
print(list(names_and_ages))

#Enumaerate
#Say we want to track the index along with the list elements
names_in_order = ["sam", "bob", "ann"]

for i, name in enumerate(names_in_order):
    print(i,name)

for name, ages in enumerate(names_and_ages):
    print(name, ages)

N = 10
matrix = [[0 for i in range(0,N)] for j in range(0,N)]
print(matrix)
#sorting
random_list = [5,1,3,4,2]

#sorted returns a new list
sorted_list = sorted(random_list)
print(sorted_list)
reverse_list = sorted(random_list, reverse = True)
print(reverse_list)

#calling .sort() modifies the list