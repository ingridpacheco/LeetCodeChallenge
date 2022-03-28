class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """

        result = []
        
        for p in path.split('/'):
            if p == "..":
                if len(result) > 0:
                    result.pop()
            elif p != '' and p != '.':
                result.append(p)
        
        return '/' + '/'.join(result)