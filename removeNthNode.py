# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
    
        
        counter = 1
        fast = head
        slow = head
        
        for counter in range(n):
            fast = fast.next
            counter += 1
        if fast is None:
            head = head.next
            head.next = head.next.next
            return
        while fast.next is not None:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head

        