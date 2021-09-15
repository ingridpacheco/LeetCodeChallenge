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
        