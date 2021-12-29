import math

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        nodes = {
            0: head
        }
        
        node = head.next
        index = 1
        
        while (node != None):
            nodes[index] = node
            index += 1
            node = node.next
            
        middle_index = math.ceil(float(index - 1)/2)
        
        return nodes[middle_index]    