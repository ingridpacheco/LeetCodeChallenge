class FreqStack(object):

    def __init__(self):
        self.list = []
        self.freq = {}
        self.num_values = {}
        self.max_value = 0
        self.val = -1

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.list.insert(0, val)
        num_value = 0
        
        if val not in self.freq:
            self.freq[val] = 1
        else:
            self.freq[val] += 1
            
        num_freq = self.freq[val]
            
        if num_freq >= self.max_value:
            self.max_value = num_freq
            self.val = val
        
        if num_freq not in self.num_values:
            self.num_values[num_freq] = [val]
        else:
            self.num_values[num_freq].insert(0,val)
        
    def pop(self):
        """
        :rtype: int
        """
        result = self.val
        
        self.freq[result] -= 1
        
        self.num_values[self.max_value].remove(result)
        
        self.list.remove(result)
        
        if len(self.num_values[self.max_value]) == 0:
            self.max_value -= 1
            
        if self.max_value > 0:
            self.val = self.num_values[self.max_value][0]
                
        return result

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()