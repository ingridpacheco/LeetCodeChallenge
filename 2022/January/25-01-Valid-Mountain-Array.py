class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        
        if len(arr) < 3:
            return False
        
        old_value = arr[0]
        opperation = -1
        
        for i in range(1,len(arr)):
            v = arr[i]
            if v > old_value:
                if opperation == -1:
                    opperation = 0
                elif opperation == 1:
                    return False
            elif v < old_value:
                if opperation == -1:
                    return False
                if opperation == 0:
                    opperation = 1
            else:
                return False
            old_value = v
            
        if opperation == 0:
            return False
        
        return True