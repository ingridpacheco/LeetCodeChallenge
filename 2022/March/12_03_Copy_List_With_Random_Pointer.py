"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        
        if head is None:
            return head
        
        node = head
        corr = {}
        
        while head is not None:
            next_node = None
            if head.next is not None:
                if head.next not in corr:
                    corr[head.next] = Node(head.next.val)
                next_node = corr[head.next]

            random = None
            if head.random is not None:
                if head.random not in corr:
                    corr[head.random] = Node(head.random.val)
                random = corr[head.random]
            
            if head not in corr:
                corr[head] = Node(head.val, next_node, random)
            else:
                if corr[head].next is None and head.next is not None:
                    corr[head].next = next_node
                    
                if corr[head].random is None and head.random is not None:
                    corr[head].random = random
            
            head = head.next
        
        return corr[node]