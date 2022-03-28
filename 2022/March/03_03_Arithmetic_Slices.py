class Solution(object):
    def numberOfArithmeticSlices(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if len(nums) < 3:
            return 0
        
        results = []
        dif = nums[len(nums)-1] - nums[len(nums)-2]
        result = [nums[len(nums)-2], nums[len(nums)-1]]
        
        for i in range(len(nums) - 3,-1,-1):
            if nums[i+1] - nums[i] == dif:
                result = result[:]
                result.insert(0, nums[i])
                if len(result) == 3:
                    results.append(result)
                else:
                    qtd = len(result)
                    while qtd >= 3:
                        results.append(result[:qtd])
                        qtd -= 1
            else:
                dif = nums[i+1] - nums[i]
                result = [nums[i],nums[i+1]]
                
        return len(results)