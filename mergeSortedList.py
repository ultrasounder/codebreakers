# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
'''
head = 1->2->4
                |

1->3->4->5->6->7
         |

                           |
Zipped list: 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6 -> 7
# pointers: head, p1, p2, cur
'''

l3 = ListNode(0) #create a new List node
curr = l3 # set curr to the new list node

while l1 and l2:
    if l2.val < l1.val:
        curr.next = l2
        l2 = l2.next
    else:
        curr.next = l1
        l1 = l1.next
    curr = curr.next
if l1:
    curr.next = l1
if l2:
    curr.next = l2
return l3.next

