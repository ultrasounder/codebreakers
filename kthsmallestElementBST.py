# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        node = root

        while stack or node:
            while node:
                stack.append(node)
                node = node.left

            stack.pop(node) # the only arguement that pop() can take is an index. No arguement defaults to the last item in the list
            k -= 1
            if k == 0:
                return node.val # we exit out of the loop after node is none, so taking None.val is going to throw an error
            node = node.right
'''
So it looks like you are trying to append these to a list and then take the n-th largest of these. There are a few problems here which I
addressed in-line. An easier approach that we can do is to do an in-order tree traversal method recursively.
Something like this is what I am thinking. I coded this up quickly so there may be other small tweaks to make, but the recursive solution
is cleaner and we actually use much less memory. Let me know if you have any questions about this problem and I would be happy
to answer them!

class Solution:
    def inOrder(self, node):
            if node == None or self.ans != None:
                return
            self.inOrder(node.left)
            self.k -= 1
            if self.k == 0:
                self.ans = node.val
            self.inOrder(node.right)
            
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.ans, self.k = None, k
        self.inOrder(root)
        return self.ans
'''                
