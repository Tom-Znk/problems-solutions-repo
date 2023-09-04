# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        """Standard Hare and Tortoise Algorithm"""

        if not head:
            return False

        hare = head
        tortoise = head

        while (hare != None) and (hare.next != None) and (tortoise!= None):

            hare = hare.next.next
            tortoise = tortoise.next

            if hare == tortoise:
                return True

        return False

            
                


