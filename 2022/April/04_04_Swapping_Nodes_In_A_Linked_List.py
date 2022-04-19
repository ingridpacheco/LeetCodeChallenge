# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        nodes = {}
        length = 0
        cur_node = head
        
        while cur_node is not None:
            length += 1
            nodes[length] = cur_node
            cur_node = cur_node.next
            
        nodes[k].val, nodes[length - k + 1].val = nodes[length - k + 1].val, nodes[k].val
        return nodes[1]
        