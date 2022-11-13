class MedianFinder:

    def __init__(self):
        self.minheap = []
        self.maxheap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxheap, -num)
        
        if len(self.maxheap) > len(self.minheap)+1:
            temp = heapq.heappop(self.maxheap)
            heapq.heappush(self.minheap, -temp)
        
        if self.minheap and self.maxheap and -self.maxheap[0] > self.minheap[0]:
            temp = heapq.heappop(self.maxheap)
            temp2 = heapq.heappop(self.minheap)
            heapq.heappush(self.minheap, -temp)
            heapq.heappush(self.maxheap, -temp2)
        
        
    def findMedian(self) -> float:
        if len(self.maxheap) == len(self.minheap):
            return  (self.minheap[0] + -self.maxheap[0])/2
        return -self.maxheap[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()