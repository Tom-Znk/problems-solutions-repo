"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        """ Storage using a Hash Table"""
        
        if not head:
            return None

        copyNode = head
        copy_storage = dict()
        while copyNode:
            copy_storage[copyNode] = Node(copyNode.val)
            copyNode = copyNode.next

        copyNode = head

        while copyNode:
            if copyNode.next:
                copy_storage[copyNode].next = copy_storage[copyNode.next]
            if copyNode.random:
                copy_storage[copyNode].random = copy_storage[copyNode.random]
            copyNode = copyNode.next

        return copy_storage[head]