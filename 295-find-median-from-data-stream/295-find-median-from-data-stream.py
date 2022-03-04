class MedianFinder:
    def __init__(self):
        self.left = []
        self.right = []
        
    def addNum(self, num: int) -> None:
        heapq.heappush(self.left, -num)
        
        if len(self.left) > len(self.right) + 1:
            leftval = -1 * heapq.heappop(self.left)
            heapq.heappush(self.right, leftval)
            
        if self.left and self.right and (-1 * self.left[0]) > self.right[0]: 
            leftval = -1 * heapq.heappop(self.left) 
            heapq.heappush(self.right, leftval)
            rightval = -1 * heapq.heappop(self.right)
            heapq.heappush(self.left, rightval)
            
    def findMedian(self) -> float:
        if len(self.left) == len(self.right):
            return ((-self.left[0]) + self.right[0])/2
        
        elif len(self.left) > len(self.right):
            return -self.left[0]
            
            
            
    
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()