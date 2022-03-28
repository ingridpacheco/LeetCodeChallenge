class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        
        last = {c: i for i,c in enumerate(s)}
        initial = 0
        max_end = 0
        res = []
        
        for i,c in enumerate(s):
            max_end = max(last[c], max_end)
            if i == max_end:
                res.append((max_end-initial) + 1)
                initial = max_end + 1
        
        return res