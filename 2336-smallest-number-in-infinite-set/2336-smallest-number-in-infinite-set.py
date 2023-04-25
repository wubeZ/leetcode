class SmallestInfiniteSet:

    def __init__(self):
        self.heap = []
        for i in range(1, 2001):
            heapq.heappush(self.heap, i)
        self.visited = set(self.heap)

    def popSmallest(self) -> int:
        val = heapq.heappop(self.heap)
        self.visited.discard(val)
        return val

    def addBack(self, num: int) -> None:
        if num not in self.visited:
            heapq.heappush(self.heap, num)
            self.visited.add(num)
        

# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)