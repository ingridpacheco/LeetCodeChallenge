class Solution {
    public int numDistinct(String s, String t) {
        int sLength = s.length(), tLength = t.length();
        if (sLength == tLength) return s.equals(t) ? 1 : 0;
        if (sLength < tLength) return 0;
        int[][] dp = new int[tLength + 1][sLength + 1];
        for (int j = 0; j <= sLength; j++) {
            dp[0][j] = 1;
        }
        
        for (int i = 0; i < tLength; i++) {
            for (int j = 0; j < sLength; j++) {
                if (s.charAt(j) == t.charAt(i)) {
                    dp[i + 1][j + 1] = dp[i][j] + dp[i + 1][j];
                } else {
                    dp[i + 1][j + 1] = dp[i + 1][j];
                }
            }
        }
        
        return dp[tLength][sLength];
    }
}