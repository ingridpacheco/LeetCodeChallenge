class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        if len(nums) != 1:
            for i in range(len(nums) - 2, -1, -1):
                if nums[i] < nums[i+1]:
                    last_sorted_part = nums[i+1:]
                    last_sorted_part.sort()
                    for ind, n in enumerate(last_sorted_part):
                        if n > nums[i]:
                            last_sorted_part[ind], nums[i] = nums[i], n
                            break
                    
                    nums[i+1:] = last_sorted_part
                    break
                elif i == 0:
                    nums.sort()