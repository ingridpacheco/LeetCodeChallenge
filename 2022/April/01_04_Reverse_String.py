class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        s_length = len(s)
        
        for i in range(int(s_length/2) + 1):
            if i < s_length - i - 1:
                first_char = s[i]
                s[i] = s[s_length - i - 1]
                s[s_length - i - 1] = first_char