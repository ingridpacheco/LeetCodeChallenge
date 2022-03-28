# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        if list1 == None and list2 == None:
            return None
        
        node = ListNode()
        prev = node
        
        while (list1 is not None and list2 is not None):
            if list2.val < list1.val:
                prev.next = list2
                list2 = list2.next
            else:
                prev.next = list1
                list1 = list1.next
            prev = prev.next
            
        if list1 == None:
            prev.next = list2
        
        if list2 == None:
            prev.next = list1
            
        return node.next