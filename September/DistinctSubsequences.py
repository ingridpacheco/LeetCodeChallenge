class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """

        s_length = len(s)
        t_length = len(t)

        if (s_length == t_length):
            return 1 if s == t else 0
        if (s_length < t_length):
            return 0

        dp = [[] for _ in range(t_length + 1)]

        for i in range(0, t_length + 1):
            if i == 0:
                dp[i] = [1 for _ in range(s_length + 1)]
            else:
                dp[i] = [0 for _ in range(s_length + 1)]

        for i in range(0, t_length):
            for j in range(0, s_length):
                if (s[j] == t[i]):
                    dp[i + 1][j + 1] = dp[i][j] + dp[i + 1][j]
                else:
                    dp[i + 1][j + 1] = dp[i + 1][j]
                
        return dp[t_length][s_length]

if __name__ == '__main__':
    resp = Solution()
    print(resp.numDistinct("rabbbit", "rabbit"))
    print(resp.numDistinct("babgbag", "bag"))