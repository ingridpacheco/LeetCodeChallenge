class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        i = 0
        exp = 2**i
        while (n > exp):
            i += 1
            exp = 2**i
            
        if n == exp:
            return True
        return False