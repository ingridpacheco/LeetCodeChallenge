# Given a binary array nums, return the maximum number of consecutive 1's in the array.
# Input: nums = [1,1,0,1,1,1]
# Output: 3

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        max_seq = 0
        cons = 0
        
        for n in nums:
            if (n == 1):
                cons = cons + 1
            else:
                cons = 0
            if (cons > max_seq):
                max_seq = cons
        
        return max_seq