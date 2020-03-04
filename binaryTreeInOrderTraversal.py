'''Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]

Follow up: Recursive solution is trivial, could you do it iteratively?'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        node = root
        inorder = []#variable length array(list)
        while stack or root:
            while root:
                stack.append(node)
                node = node.left
            
            node = stack.pop()
            inorder.append(node.val)
            node = node.right
        return inorder


