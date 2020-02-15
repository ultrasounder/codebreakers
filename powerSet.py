def powerset(array):
    subsets = [[]]
    for ele in array:
        for i in range(len(subsets)):
            currentSubsets = subsets[i]
            subsets.append(currentSubsets + [ele])
    return subsets
