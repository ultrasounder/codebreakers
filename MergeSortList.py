# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# Find the middle of the linked list
# divide into 2 linkedlists and sort each
# merge the linkedlist in the right order

# Base case:
#   if not head or not head.next -> head

#reducing the input size 
# reducing by half (dividing the linkedlist into 2)
# using a slow and a fast pointers


class Solution:
    def sortList(self, head: ListNode) -> ListNode:

        def merge(left, right):
            dummy = ListNode(0)
            curr = dummy
            while left and right:
                if left.val < right.val:
                    curr.next = left
                    left = left.next
                else:
                    curr.next = right
                    right = right.next
                curr = curr.next
            curr.next = left or right
            return dummy.next

        if not head or not head.next:
            return head
        prev = None
        slow = head
        fast = head
        while fast and fast.next:
            prev = slow # Make prev the tail of the slow
            slow = slow.next # Slow moves one position ahead of prev
            fast = fast.next.next #Fast moves two ahead of slow
        prev.next = None # Cut the list into two halves after the Prev, slow and fast have traversed

        left = self.sortList(head)
        right = self.sortList(slow)
        return merge(left, right)