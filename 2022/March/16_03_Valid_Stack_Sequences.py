class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        
        index = -1
        
        num = popped.pop(0)
        
        for i in range(len(pushed)):
            if pushed[i] == num:
                index = i
                pushed.pop(index)
                break
        
        while len(popped) > 0:
            num = popped.pop(0)
            
            if (index - 1 >= 0) and pushed[index-1] == num:
                index = index - 1
                pushed.pop(index)
                continue
                
            if index >= len(pushed):
                return False
            
            for i in range(index, len(pushed)):
                if pushed[i] == num:
                    index = i
                    pushed.pop(index)
                    break
                    
            if len(pushed) > len(popped):
                return False
                    
        return True