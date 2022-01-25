# You are given an integer n. You have an n x n binary grid grid with all values initially 1's except 
# for some indices given in the array mines. The ith element of the array mines is defined as mines[i] = [xi, yi] 
# where grid[xi][yi] == 0.

# Return the order of the largest axis-aligned plus sign of 1's contained in grid. If there is none, return 0.

# An axis-aligned plus sign of 1's of order k has some center grid[r][c] == 1 along with four arms of 
# length k - 1 going up, down, left, and right, and made of 1's. Note that there could be 0's or 1's beyond 
# the arms of the plus sign, only the relevant area of the plus sign is checked for 1's.

# Ex:
#   Input: n = 5, mines = [[4,2]]
#   Output: 2

from bisect import bisect_right

class Solution(object):
    def orderOfLargestPlusSign(self, N, mines):
        """
        :type N: int
        :type mines: List[List[int]]
        :rtype: int
        """
        rows = [[-1, N] for _ in xrange(N)]
        cols = [[-1, N] for _ in xrange(N)]
        
        for r, c in mines:
            rows[r].append(c)
            cols[c].append(r)

        for i in xrange(N):
            rows[i].sort()
            cols[i].sort()
        mxp = 0
        for r in xrange(N):
            for i in xrange(len(rows[r])-1):
                left_b = rows[r][i]
                right_b = rows[r][i+1]
                for c in xrange(left_b+mxp+1, right_b-mxp):
                    idx = bisect_right(cols[c], r)-1
                    up_b = cols[c][idx]
                    down_b = cols[c][idx+1]
                    mxp = max(mxp, min(c-left_b, right_b-c, r-up_b, down_b-r))
        return mxp
        