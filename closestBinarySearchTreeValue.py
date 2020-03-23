'''270. Closest Binary Search Tree Value
Easy

569

45

Add to List

Share
Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.

Note:

Given target value is a floating point.
You are guaranteed to have only one unique value in the BST that is closest to the target.
Example:

Input: root = [4,2,5,1,3], target = 3.714286

    4
   / \
  2   5
 / \
1   3

Output: 4'''

# Definition for a binary tree node.
#O(log(N)) time and O(N) space
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        return ClosestValueHelper(root, target, float("inf"))
    

    def ClosestValueHelper(self, root, target, closest):
        if root is None:
            return closest
        if abs(target - closest) > abs(target - root.val):
            closest = root.val
        if target < root.val:
            return ClosestValueHelper(root.left, target, closest)
        elif target > root.val:
            return ClosestValueHelper(root.right, target, closest)
        else:
            return closest





