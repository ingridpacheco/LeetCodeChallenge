class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        
        while left < right:
            if s[left] != s[right]:
                left_pos = s[left:right]
                right_pos = s[left+1:right+1]
                return left_pos == left_pos[::-1] or right_pos == right_pos[::-1]
            left += 1
            right -= 1

        return True

if __name__ == "__main__":
    s = Solution()
    print(s.validPalindrome("ebcbbececabbacecbbcbe"))
    print(s.validPalindrome("abba"))
    print(s.validPalindrome("acbba"))
    print(s.validPalindrome("abbac"))
    print(s.validPalindrome("acbbad"))