class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        
        #[[1,1,0,0,0],
        #[1,1,1,1,0],
        #[1,0,0,0,0],
        #[1,1,0,0,0],
        #[1,1,1,1,1]],

        soldiers = {}

        for i, row in enumerate(mat):
            column = 0
            while column < len(row) and row[column] == 1:
                column += 1
            if column not in soldiers:
                soldiers[column] = [i]
            else:
                soldiers[column].append(i)
        
        res = []
        for key in sorted(soldiers):
            for index in soldiers[key]:
                res.append(index)
                if len(res) == k:
                    return res