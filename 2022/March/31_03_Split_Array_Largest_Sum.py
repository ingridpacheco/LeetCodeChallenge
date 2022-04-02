class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        max_sum = sum(nums)
        max_element = max(nums)
        result = 0
                
        while max_element <= max_sum:
            max_possible_sum = int((max_sum + max_element)/2)
            splits = 0
            curr_sum = 0
            for number in nums:
                if curr_sum + number > max_possible_sum:
                    curr_sum = number
                    splits += 1
                    if splits >= m:
                        break
                else:
                    curr_sum += number
            
            if splits < m:
                max_sum = max_possible_sum - 1
                result = max_possible_sum
            else:
                max_element = max_possible_sum + 1
                
        return result