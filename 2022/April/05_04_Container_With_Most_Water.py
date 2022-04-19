class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        max_water = 0
        left = 0
        right = len(height) - 1
        
        while right > left:
            h1 = height[left]
            h2 = height[right]
            size = right - left
            height_dif = min(h1,h2)
            amount_water = size * height_dif
            if amount_water > max_water:
                max_water = amount_water
            
            if h1 != h2:
                if height_dif == h1:
                    left += 1
                else:
                    right -= 1
            else:
                if height[left + 1] > height[right - 1]:
                    left += 1
                else:
                    right -= 1
                    
        return max_water