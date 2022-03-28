class Solution(object):
    def change_max_distance(self, max_distance, distance):
        if max_distance == 0 or distance > max_distance:
            return distance
        return max_distance
    
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        max_distance = 0
        
        idx1 = -1
        
        for i in range(len(seats)):
            if seats[i] == 1:
                if idx1 == -1 and i == 0:
                    idx1 = i
                elif idx1 == -1:
                    idx1 = i
                    distance = (idx1 - 0)
                    max_distance = self.change_max_distance(max_distance, distance)
                else:
                    distance = (i - idx1) // 2
                    max_distance = self.change_max_distance(max_distance, distance)
                    idx1 = i
            elif i == (len(seats) - 1):
                distance = (i - idx1)
                max_distance = self.change_max_distance(max_distance, distance)
                
        return max_distance