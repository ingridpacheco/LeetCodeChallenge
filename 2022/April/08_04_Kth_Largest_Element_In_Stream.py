class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.list = nums
        self.k = k
        self.list.sort(reverse=True)
        self.list = self.list[:k]

    def add(self, val: int) -> int:
        if len(self.list) == 0:
            self.list.append(val)
        elif val >= self.list[0]:
            self.list.insert(0,val)
        elif val <= self.list[len(self.list) - 1]:
            self.list.append(val)
        else:
            left = 0
            right = len(self.list) - 1
            
            while left < right:
                middle = int((left + right)/2)
                if val > self.list[middle]:
                    if val <= self.list[middle - 1]:
                        self.list.insert(middle, val)
                        break
                    else:
                        right = middle - 1
                elif val < self.list[middle]:
                    if val >= self.list[middle + 1]:
                        self.list.insert(middle + 1, val)
                        break
                    else:
                        left = middle + 1
                else:
                    self.list.insert(middle, val)
                    break
                    
        return self.list[self.k - 1]
            
        
# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)