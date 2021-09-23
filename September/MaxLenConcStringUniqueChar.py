# Given an array of strings arr. String s is a concatenation of a sub-sequence of arr which have unique characters.

# Return the maximum possible length of s.

# Ex:

#   Input: arr = ["un","iq","ue"]
#   Output: 4

class Solution(object):
    def maxLength(self, arr):
        """
        :type arr: List[str]
        :rtype: int
        """
        
        if (len(arr) == 1):
            return len(arr[0])
        
        results = [""]
        max_word = 0
        for word in arr:
            for i in range(len(results)):
                new_res = results[i] + word
                if len(new_res) != len(set(new_res)):
                    continue

                results.append(new_res)
                max_word = max(max_word, len(new_res))
        return max_word   