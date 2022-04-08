class KthLargest(object):

    def __init__(self, k, nums):
        self.nums = nums
        self.k = k
        heapq.heapify(self.nums)
    def add(self, val):
        heapq.heappush(self.nums, val)
    
        for i in range(self.k):
            if self.k < len(self.nums):
                heapq.heappop(self.nums)
        
        return self.nums[0]
    
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)