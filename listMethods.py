earnings = [91, 87, 115, 108]

for amnt in earnings:
    print(amnt)

for amnt in range(4):
    print("You make", earnings[amnt], "thousand dollars a year")


for i in range(len(earnings)):
    print(earnings[i])

USD_to_CND = 1.13

# for amnt in earnings:
#     amnt *= USD_to_CND
#     print('amnt is now', amnt)

# print('earnings is now', earnings)

for i in range(len(earnings)):
    earnings[i] *= USD_to_CND

print(earnings)
L = [9, 8, 7, 6, 5, 4, 3, 10, 15, 17, 18]
def manual_slice(L, i, j, step):
    newL = []
    for ind in range(i, j, step):
        newL.append(L[ind])
    return newL



numbers = [1, 2, 3, 4, 5]

for index in range(len(numbers)):
    numbers[index] = numbers[index] ** 2        

for index, value in enumerate(['banana','apple','pear','quince']):
    print(index, value)


def double_stuff(a_list):
    for index, value in enumerate(a_list):
        a_list[index] = 2 * value
        print(a_list[index])


def recursive_sum(nested_number_list):
    sum = 0
    for element in nested_number_list:
        if type(element) == type([]):
            sum += recursive_sum(element)
        else:
            sum += element
    return sum

print(recursive_sum([2, 9, [1, 13], 8, 6]))

def recursive_max(nested_number_list):
    largest = nested_number_list[0]
    while type(largest) == type([]):
        largest = largest[0]


    for element in nested_number_list:
        if type(element) == type([]):
            max_of_elem = recursive_max(element)
            if largest < max_of_elem:
                largest = max_of_elem
            else:
                if largest < element:
                    largest = element
    return largest
print(recursive_max([2, 9, [1, 13], 8, 6]))


def find_max(seq, max_so_far):
    if not seq:
        return max_so_far
    if max_so_far < seq[0]:
        return find_max(seq[1:], seq[0])
    else:
        return find_max(seq[1:], max_so_far)
print(find_max([2, 9, [1, 13], 8, 6]))      

