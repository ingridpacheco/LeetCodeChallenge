# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def deal_number(self, number_sum, increment):
        if increment:
            number_sum += 1
            increment = False
        if number_sum >= 10:
            number_sum = number_sum - 10
            increment = True
        return number_sum, increment
    def addTwoNumbers(self, l1, l2, increment=False):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = ListNode()

        if l1 is not None and l2 is not None:
            number_sum = l1.val + l2.val
            number_sum, increment = self.deal_number(number_sum, increment)
            l1 = l1.next
            l2 = l2.next
            ListNode
            result.val = number_sum
            result.next = self.addTwoNumbers(l1,l2,increment)
        elif l1 is not None:
            result.val, increment = self.deal_number(l1.val, increment)
            l1 = l1.next
            result.next = self.addTwoNumbers(l1,l2,increment)
        elif l2 is not None:
            result.val, increment = self.deal_number(l2.val, increment)
            l2 = l2.next
            result.next = self.addTwoNumbers(l1,l2,increment)
        elif increment:
            result.val = 1
            result.next = None   
        else:
            return None
            
        return result