from queue import Queue
'''Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:

[
  [3],
  [9,20],
  [15,7]
]
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:

        result = []

        if root is None:
            return result

        Q = Queue() # python lists with pop and append are stacks. We should not be using it as a queue. Also, variables should be lowercase. We also want to be passing in root node in
        Q.put(root)#add root node
        while Q is not None: # while it isn't empty. We can still have a empty queue but we are still pointing to an object
            size = Q.qsize()#get the size of the queue

            currentLevel = []#initalize a list to hold the elements of current level

            for i in range(size):
                current = Q.get() # this is the last element. We want to be popping the first element in the list (deque)
                currentLevel.append(current.val)
                if current.left is not None:
                    Q.put(current.left)
                if current.right is not None:
                    Q.put(current.right) # nice checks on lines 45-48
            result.append[currentLevel]
        return result
        
        '''
        Nice idea with this approach. The queue vs stack implementation is going to give you the wrong answer. If you fix this 
        then the solution should be correct. Look through the notes and message me if you have any questions about them! You have the
        right approach which is the hardest part. Just change your implementation a bit and you'll be set!
        '''



