# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow
'''
Great solution. This is exactly what we want to be doing. We do this in one pass with constant memory.
There is no way to index a linked list so this has to be the best solution. Nice work!
'''
