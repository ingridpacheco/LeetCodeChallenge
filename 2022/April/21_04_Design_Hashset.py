class MyHashSet:

    def __init__(self):
        self.list = {}
        
    def add(self, key: int) -> None:
        if key not in self.list:
            self.list[key] = 1

    def remove(self, key: int) -> None:
        if key in self.list:
            del self.list[key]

    def contains(self, key: int) -> bool:
        return key in self.list
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)