class Solution(object):
    def getSmallestString(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """

        res = ''
        
        while (n-1) > 0 and (k-1)/(n-1) < 26:
            res += 'a'
            k -= 1
            n -= 1
            
        mis = k - (26*(n-1))
        res += chr(96 + mis)
        if n-1 > 0:
            res += (n-1) * 'z'
        
        return res