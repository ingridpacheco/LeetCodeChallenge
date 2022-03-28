class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        if len(s) == 0:
            return True
        elif len(t) == 0:
            return False
        else:
            i = 0
            result = False

            for char in t:
                if char == s[i]:
                    if i == len(s) - 1:
                        result = True
                        break
                    else:
                        i += 1
            return result