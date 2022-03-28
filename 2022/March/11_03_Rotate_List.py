# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        
        if head is None or k == 0:
            return head
        
        nodes = {}
        length = 0
        node = head
        
        while node is not None:
            nodes[length] = node
            node = node.next
            length += 1
            
        k = k % length
        
        if k == 0:
            return head
            
        nodes[length - k - 1].next = None
        nodes[length - 1].next = nodes[0]
        
        return nodes[length - k]