class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq._heapify_max(nums)
        
        for i in range(k-1):
            heapq.heappop(nums)
            heapq._heapify_max(nums)
        
        return nums[0]