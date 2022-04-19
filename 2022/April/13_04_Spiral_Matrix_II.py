class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        
        #n=2 => [[1,2],[4,3]]
        #n=4 => [[1,2,3,4],[12,13,14,5],[11,16,15,6],[10,9,8,7]]
        
        matrix = [[None for i in range(n)] for j in range(n)]
        top = 0
        bottom = n - 1
        left = 0
        right = n - 1
        
        number = 1
        
        i = 0
        j = 0
        
        direction = "right"
        
        while matrix[i][j] is None:
            while direction == "right":
                if i < 0 or i >= n or j <0 or j >= n or matrix[i][j] is not None:
                    return matrix
                matrix[i][j] = number
                number += 1
                j += 1
                if j > right:
                    i += 1
                    j -= 1
                    top += 1
                    direction = "down"
                    
            while direction == "down":
                if i < 0 or i >= n or j <0 or j >= n or matrix[i][j] is not None:
                    return matrix
                matrix[i][j] = number
                number += 1
                i += 1
                if i > bottom:
                    j -= 1
                    i -= 1
                    right -= 1
                    direction = "left"
                
            while direction == "left":
                if i < 0 or i >= n or j <0 or j >= n or matrix[i][j] is not None:
                    return matrix
                matrix[i][j] = number
                number += 1
                j -= 1
                if j < left:
                    j += 1
                    i -= 1
                    bottom -= 1
                    direction = "up"
                
            while direction == "up":
                if i < 0 or i >= n or j < 0 or j >= n or matrix[i][j] is not None:
                    return matrix
                matrix[i][j] = number
                number += 1
                i -= 1
                if i < top:
                    i += 1
                    j += 1
                    left += 1
                    direction = "right"
        
        return matrix