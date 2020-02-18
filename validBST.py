# Given a binary tree, determine if it is a valid binary search tree (BST).

# Assume a BST is defined as follows:

# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
 

# Example 1:

#     2
#    / \
#   1   3

# Input: [2,1,3]
# Output: true
# Example 2:

#     5
#    / \
#   1   4
#      / \
#     3   6

# Input: [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''we want to traverse in-order as the tree is sorted in-order if you go left,root and then right'''

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # stack = []
        # left_child_val = float('inf')

        # while stack is not None or root is not None:
        #     while stack is not None:
        #         stack.append(root)
        #         root = root.left
            
        #     root = stack.pop()
        #     if root.val <= left_child_val:
        #         return False
        #     left_child_val = root.val
        #     root = root.right



        # return True
#validate BST, the formulae for the value of any child node is;  
#   10 <= Node.value  < 10  10 <= Node.value < 15 time complexity O(N) and space complexity O(d), where d is the depth of the 
# longest branch of the treee
# 

    #        10
    #     5       15
    #  2     5  13   22
    # 1            14

def validateBst(root):
    return _validateBstHelper(root, float("-inf"), float("inf"))

def _validateBstHelper(tree, minValue, maxValue):
    if tree is None:
        return True
    if tree.value < minValue    or tree.value > maxValue:
        return False
    leftIsValid = _validateBstHelper(tree.left, minValue, tree.value)
    return leftIsValid and _validateBstHelper(tree.right, tree.value, maxValue)




def validate(root):
    return helper(root, float('inf'), -float('inf'))

def helper(root, ceiling, floor):
    if root == None:
        return True
    if root.val > ceiling or root.val < floor:
        return False
    return helper(root.left, min(root.val, ceiling), floor) and helper(root.right, ceiling, max(root.val, floor))
