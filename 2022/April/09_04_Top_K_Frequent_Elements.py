class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        if len(nums) == 1:
            return nums
        
        frequency = {}

        for number in nums:
            if number in frequency:
                frequency[number] += 1
            else:
                frequency[number] = 1
        
        sorted_frequency = [key for (key,value) in sorted(frequency.items(), key=lambda x:x[1], reverse=True)]
        
        return sorted_frequency[:k]