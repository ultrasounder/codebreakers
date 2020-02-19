#time complexity O(log(N)) worst O(N)
#space complexity Iterative solution O(1)

def findClosestValueInBst(tree, target):
    return findClosestValueInBstHelper(tree, target, float("inf"))

def findClosestValueInBstHelper(tree, target, closest):
    if tree is None:
        return closest
    if abs(target - closest) > abs(target - tree.value):
        closest = tree.value
    if target < tree.value:
        return findClosestValueInBstHelper(tree.left, target, closest) # shouldn't this be tree.left?
    elif target > tree.value:
        return findClosestValueInBstHelper(tree.right, target, closest)
    else:
        return closest
    
    '''
    Nice solution. The run time will only be log(N) for a balanced tree. I m assuming you meant this when you wrote 
    out the runtimes for the proiblem. Nice job using the helper method. We see how effective this is in tackling recursive solutions.
    Looks like it will return the right answer aside from the small bug I pointed out. Good work!
    '''
