# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        node = head
        
        while (node is not None and node.val is not False):
            node.val = False
            node = node.next
            
        if node is None:
            return False
        
        return True