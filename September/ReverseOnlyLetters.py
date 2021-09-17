# Given a string s, reverse the string according to the following rules:

# All the characters that are not English letters remain in the same position.
# All the English letters (lowercase or uppercase) should be reversed.
# Return s after reversing it.

# Ex:
#   Input: s = "ab-cd"
#   Output: "dc-ba"

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