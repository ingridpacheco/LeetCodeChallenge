class Solution(object):
    
    def getSubStringValue(self, i, prev, s): 
        c = s[i]
        total = 0
        
        if c == "(":
            result = self.getSubStringValue(i+1,c,s)
            i = result[1]
            if result[0] == -1:
                total = 1
            else:
                total = 2 * result[0]
        else:
            if prev == '(':
                return -1, i
            
        if (i+1 < len(s)) and s[i+1] == "(":
            result = self.getSubStringValue(i+1,s[i],s)
            total += result[0]
            i = result[1]
        else:
            i += 1
        
        return total, i
    
    def scoreOfParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        result = self.getSubStringValue(0, None, s)
        return result[0]