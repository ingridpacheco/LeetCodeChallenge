# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        
        if len(lists) == 0:
            return None
        
        new_node = ListNode()
        res = new_node
        
        min_value = None
        index = 0
        
        indexes = {}
        
        for i in range(len(lists)):
            if lists[i] != None:
                if lists[i].val not in indexes:
                    indexes[lists[i].val] = [i]
                else:
                    indexes[lists[i].val].append(i)    
        
        while len(indexes.keys()) > 0:
            min_key = sorted(indexes)[0]
            for i in indexes[min_key]:
                lists[i] = lists[i].next
                if lists[i] != None:
                    if lists[i].val not in indexes:
                        indexes[lists[i].val] = [i]
                    else:
                        indexes[lists[i].val].append(i)
                res.next = ListNode(min_key)
                res = res.next
            del indexes[min_key]
            
        return new_node.next