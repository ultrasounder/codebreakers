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

        Queue = [self]

        while Queue is not None:
            size = len(Queue)

            currentLevel = []

            for i in range(size):
                current = Queue.pop()
                currentLevel.append(current.val)
                if current.left is not None:
                    Queue.append(current.left)
                if current.right is not None:
                    Queue.append(current.right)
        result.append[currentLevel]



