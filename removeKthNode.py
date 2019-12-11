# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int ) -> ListNode:
        counter = 1
        fast = head
        slow = head
        for counter in range(n):
            fast = fast.next
            count += 1
        if fast is None:
            head = head.next
            head.next = head.next.next
        while fast.next is not None:
            fast = fast.next
            slow = slow.next
            slow,next = slow.next.next
        return head