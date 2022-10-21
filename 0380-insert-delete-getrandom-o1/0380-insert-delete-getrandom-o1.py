from random import randint
class RandomizedSet:

    def __init__(self):
        self.start = 0
        self.nums = []
        self.indices = {}
        

    def insert(self, val: int) -> bool:
        if val not in self.indices:
            self.nums.append(val)
            self.indices[val] = len(self.nums)-1
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.indices:
            idx = self.indices[val]
            self.nums[idx], self.nums[self.start] = self.nums[self.start], self.nums[idx]
            self.indices[self.nums[idx]] = idx
            del self.indices[val]
            self.start += 1
            return True
        return False

    def getRandom(self) -> int:
        idx = randint(self.start, len(self.nums)-1)
        return self.nums[idx]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()