class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        while len(stones) > 1:
            stones.sort(reverse=True)
            max_stone1 = stones[0]
            max_stone2 = stones[1]
            
            if max_stone1 == max_stone2:
                stones.pop(0)
                stones.pop(0)
            else:
                resulting_value = max_stone1 - max_stone2
                stones.pop(0)
                stones.pop(0)
                stones.append(resulting_value)
        
        return stones[0] if len(stones) > 0 else 0