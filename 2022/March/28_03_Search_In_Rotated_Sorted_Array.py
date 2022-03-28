class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        
        if len(nums) == 1:
            return nums[0] == target
        
        for index in range(len(nums)/2 + 1):
            last_index = len(nums) - index - 1
            if target == nums[index] or target == nums[last_index]:
                return True
            elif last_index <= index:
                return False