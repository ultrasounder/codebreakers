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

def merge(l1, l2):
    