#First part to determine if there is an intersection of linkedlists

# Both A and B are linked lists:
#       sf                        
#  A = {dummy, 1, 3, 5, 7, 9, 11}, k = 6
#                   |
#  B = {2, 4, 9, 11}
 
 

     

#Remove the k-th node

# def removeKthNode(head, k):
# 	dummy = Node(0)
#   dummy.next = head
# 	fast = dummy
#   slow = dummy
  
#   for i in range(k + 1):
#   	fast = fast.next

#   while fast:
#   	slow = slow.next
#     fast = fast.next
#   slow.next = slow.next.next
#   return dummy.next
  
#Palindrome line
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        vals = []
        while head:
            vals += head.next
            head = head.next
        return vals == vals[::-1]


class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


    def removeKthNodeFromEnd(self, head, k):
        counter = 1
        fast = self.head
        slow = self.head
        

        for counter in range(k):
            fast = fast.next
            counter += 1
        if fast is None:
           head.value = head.next.value
           head.next = head.next.next 
           return
        while fast.next is not None:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        














