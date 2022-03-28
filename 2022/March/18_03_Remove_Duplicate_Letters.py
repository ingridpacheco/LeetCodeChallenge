class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        letters = {}
        vis = {}

        for i in s:
            if i in letters:
                letters[i] += 1
            else:
                letters[i] = 1

        res = []

        for i in range(len(s)):
            l = s[i]
            letters[l] -= 1
            
            if l not in vis or vis[l] == 0:
                while (len(res) > 0 and res[-1] > s[i] and letters[res[-1]] > 0):
                    vis[res[-1]] = 0
                    del res[-1]

                res += s[i]
                vis[l] = 1
                
        return "".join(res)