class MyHashSet:
    
    def __init__(self):
        self.key_space = 2500
        self.set = [[] for _ in range(self.key_space)]

    def add(self, key: int) -> None:
        mod = key%self.key_space
        if key not in self.set[mod]:
            self.set[mod].append(key)

    def remove(self, key: int) -> None:
        mod = key% self.key_space
        for i, num in enumerate(self.set[mod]):
            if num == key:
                self.set[mod][i] = -1
                break
                
    def contains(self, key: int) -> bool:
        mod = key% self.key_space
        if key in self.set[mod]:
            return True
        return False
        
# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)