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
            leftmost_positions.get(depth, self.x) # what is this intended to do? Where are we getting self.x from?
            max_width = max(max_width, position - leftmost_positions.get(depth) + 1)

            _get_widths(root.left, depth + 1, position * 2)
            _get_widths(root.right, depth +1, position * 2 + 1)
            
            '''
            Hi Ananth. I am a bit confused at your approach here. Why do we need depth? It seems like we could just start at position 0
            and then everytime we move left in our tree we move the position -1 and every time we move right we move the position +1.
            We keep track of the highest and lowest these go and then we are able to return this. In the case that we need to get the 
            width of a given level, we can just use our level order traversal approach which gets us a nice level by level print out
            of the tree. Let me know if you have nay more questions regarding this problem.
            '''

        

