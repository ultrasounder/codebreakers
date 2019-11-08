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