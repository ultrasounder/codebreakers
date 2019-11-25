def recursive_sum(nest_num_list):
    sum = 0
    for element in nest_num_list:
        if type(element) == type([]):
            sum += recursive_sum(element)
        else:
            sum += element
    return sum

print(recursive_sum([1,2,3,4]))