class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        
        result = []

        for i in range(n + 1):
            count = 0
            n = i
            while (n):
                count += n & 1
                n >>= 1
            result.append(count)
            
        return result