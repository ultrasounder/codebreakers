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

random_list.sort()
print(random_list)

#one can also sort lists using custom key lambda

class Person:
    def __init__(self, name, age):
        self.age = age
        self.name = name
#provide a string representation of this object

    def __repr__(self):
        return repr((self.name), (self.age))
bob = Person("Bob",14)
sam = Person("Sam", 12)
ann = Person("Ann", 16) 

people = [bob, sam,ann]

#Sort the list by first name
people.sort(key = lambda x: x.name)
# print(people)
people.sort(key = lambda x: x.age)
# print(people)


# With strings, we can join and split to convert to and from lists and strings.
sentence_with_dashes = "The-fox-jumped-over-the-moon"
words = sentence_with_dashes.split("-")
print(words)
space_character = " "
sentence_with_spaces = space_character.join(words)
print(sentence_with_spaces)

#python dict is the most similar to a hashmap with key value pairs. The keys can be any data type as long as they are hashable

name_to_age_map = {}#empty dict

name_to_age_map["Ann"] = 16#accessing a dict using its index like list
name_to_age_map["Bob"] = 12
name_to_age_map["sam"] = 14

# .keys returns a list of all keys in the dictionary

print(name_to_age_map.keys())

#.values returns a list of all values associated with corresponding keys in the dictionary

print(name_to_age_map.values())

#.itmes() returns a list off all the keys and their corresponding values as a list of tuples    

print(name_to_age_map.items())

#we can check if a key is in the dictionary with O(1) time

print("Ryan" in name_to_age_map)

print("Sam" in name_to_age_map)

print("sam" in name_to_age_map)

#we can check value for a given key in O(1) time. It will return none if the key is not in the dictionary

print("Ryan" in name_to_age_map) 

#directly accessing a key that does not exist will result in an error.

#name_to_age_map["Ryan"]

#!!!Warning!!! This will cost you O(n) as it looks through the list, not the dictionary
"sam" in name_to_age_map.keys()


"""Python set is the most similar to Hashset. Objects added must be hashable(Key and value pair). ONce can also eprform
basic set operations"""

even_num_set = set() #create an empty 
even_num_set.add(2) # O(1)
even_num_set.add(4) #O(1)
odd_num_set = set()
odd_num_set.add(1)
odd_num_set.add(3)

3 in even_num_set #O(1)

4 in even_num_set#O(1)

#we can do set union as well in O(m+n) time. returns a list

union_num_set = even_num_set.union(odd_num_set) 
print(union_num_set)

#we can also do set intersection as well in  O(m+n) timr
intersect_num_set = even_num_set.intersection(odd_num_set)
print(intersect_num_set)

difference_set = union_num_set.difference(even_num_set)

print(difference_set)

# Heap PQ
# To implement a priority queue in Python, use the heapq library. It will use an empty list and will use that to construct
# a heap .

import heapq
heap = []

#This heapq.heappush(item) ensures that heap[0] is the SMALLEST element.
#heappush() takes O(log n) time.
heapq.heappush(heap, 3)
heapq.heappush(heap, 5)
heapq.heappush(heap, 1)

#heappop() takes O(log n) time.
min_element = heapq.heappop(heap)
print(min_element) # 1
min_element = heapq.heappop(heap)
print(min_element)
min_element = heapq.heappop(heap)
print(min_element)

# If you have tuples , it will sort with the first element and use the second element for ties

heap = []
heapq.heappush(heap, (5, 'write code'))
heapq.heappush(heap, (7, 'release product'))
heapq.heappush(heap, (1, 'write spec'))
heapq.heappush(heap, (3, 'create tests'))
heapq.heappop(heap)

# Alternatively, you have a class and want to add them to heapq. You will need to implement a '__lt__' (less than) comparator method

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

        #compare by name first, then by age if there a tie

        def __lt__(self, other):
            if self.name == other.name:
                return self.age < other.age
            return self.name < other.name

heap = []

heapq.heappush(heap, Person("Anne", 16))
heapq.heappush(heap, Person("Bob", 14))
heapq.heappush(heap, Person("Sam", 12))
heapq.heappop(heap)
#Heres how to setup a heap of fixed size. Heres an example
max_size = 20
heap = []
for i in range(0, 100):
    if len(heap) >= 20:
        heapq.heappushpop(heap, i)
    else:
        heapq.heappush(heap, i)
print(len(heap))

#If you want to use a max heap, try the following. You can either change the '__lt__' function of your class
#Alternatively you can also use heappush_max function

max_heap = []
heapq._heappush_max(max_heap, Person("Ann", '16'))
heapq._heappush_max(max_heap, Person("Bob", 14))
heapq._heappush_max(max_heap, Person("sam", 12))
heapq._heappushpop_max(max_heap)
  
