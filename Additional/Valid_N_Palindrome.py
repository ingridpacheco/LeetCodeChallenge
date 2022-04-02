class Solution:
    def runWord(self, n: int, counter: int, word: str) -> bool:
        left = 0
        right = len(word) - 1

        while left < right:
            if word[left] != word[right]:
                counter += 1
                if counter > n:
                    return False
                left_pos = word[left:right]
                right_pos = word[left+1:right+1]
                return self.runWord(n,counter,left_pos) or self.runWord(n,counter,right_pos)
            left += 1
            right -= 1

        return True

    def validPalindrome(self, n: int, s: str) -> bool:
        return self.runWord(n,0,s)

if __name__ == "__main__":
    s = Solution()
    print(s.validPalindrome(1,"ebcbbececabbacecbbcbe"))
    print(s.validPalindrome(1,"abba"))
    print(s.validPalindrome(1,"acbba"))
    print(s.validPalindrome(1,"abbac"))
    print(s.validPalindrome(1,"acbbad"))
    print(s.validPalindrome(2,"acbbad"))