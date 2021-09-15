class Solution(object):
    def reverseOnlyLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        s = list(s)
        
        index = len(s) - 1
        
        for i, v in enumerate(s):
            if i >= index:
                break
            if v.isalpha() == True:
                for j in range(index, -1, -1):
                    m = s[j]
                    if m.isalpha() == True:
                        s[i] = m
                        s[j] = v
                        index = j - 1
                        break
            
        return ''.join(s)