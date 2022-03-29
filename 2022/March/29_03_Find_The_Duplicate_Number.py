class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        listed_numbers = {}
        
        for number in nums:
            if number in listed_numbers:
                return number
            listed_numbers[number] = True