from sortedcontainers import SortedList
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.arr = SortedList()
        self.k = k
        for num in nums:
            self.arr.add(num)
        

    def add(self, val: int) -> int:
        self.arr.add(val)
            
        return self.arr[-self.k]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)