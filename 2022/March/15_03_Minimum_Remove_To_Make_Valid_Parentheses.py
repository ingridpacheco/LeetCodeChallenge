class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        result = []
        parenthesis = []
        indexes = {}

        for c in s:
            if c == '(':
                result.append(c)
                parenthesis.append(c)
                if c in indexes:
                    indexes[c].append(len(result) - 1)
                else:
                    indexes[c] = [len(result) - 1]
            elif c == ')':
                if len(parenthesis) > 0 and parenthesis[len(parenthesis) - 1] == '(':
                    result.append(c)
                    parenthesis.pop()
                    indexes['('].pop()
            else:
                result.append(c)
                
        if len(parenthesis) > 0:
            for p in parenthesis:
                if len(result) > 0:
                    ind = indexes[p].pop()
                    result.pop(ind)
                    
        return ''.join(result)