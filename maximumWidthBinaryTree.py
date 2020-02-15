# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        leftmost_positions = {}
        max_width = 0
        _get_widths(root, 0, 0)
        return max_width

        
        
        
        
        def _get_widths(root, depth, position):
            if root == None:
                return 0
            leftmost_positions.get(depth, self.x)
            max_width = max(max_width, position - leftmost_positions.get(depth) + 1)

            _get_widths(root.left, depth + 1, position * 2)
            _get_widths(root.right, depth +1, position * 2 + 1)





        

