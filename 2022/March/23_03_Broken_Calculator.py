class Solution(object):
    def brokenCalc(self, startValue, target):
        """
        :type startValue: int
        :type target: int
        :rtype: int
        """
        
        operations = 0
        
        while target != startValue:
            if target < startValue:
                operations += startValue - target
                break
            elif target % 2 != 0:
                target += 1
            else:
                target = target / 2
            operations += 1
            
        return operations