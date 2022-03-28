class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        min_index = 0
        max_index = len(nums) - 1
        
        while min_index <= max_index and min_index >= 0 and max_index <= len(nums) - 1:
            middle = min_index + (max_index - min_index) / 2
            cur_num = nums[middle]
            if cur_num > target:
                max_index = middle - 1
            elif cur_num < target:
                min_index = middle + 1
            else:
                return middle
        return -1