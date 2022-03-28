class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        
        people.sort()
        lp = 0
        rp = len(people) - 1
        
        boats = 0
        
        while lp <= rp:
            if people[lp] + people[rp] <= limit:
                lp += 1
                
            rp -= 1
            boats += 1
                
        return boats