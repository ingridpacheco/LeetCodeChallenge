class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        rows = len(matrix)
        columns = len(matrix[0])
        
        m = 0
        
        while m < rows and target > matrix[m][columns - 1]:
            m += 1
            
        if m >= rows or target < matrix[m][0]:
            return False
        
        for c in range(columns):
            if matrix[m][c] == target:
                return True
            
        return False