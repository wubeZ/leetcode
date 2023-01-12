class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        heap = [ -num for num in nums ]
        heapq.heapify(heap)
        ans = 0
        
        for _ in range(k):
            val = -1*heapq.heappop(heap)
            ans += val
            val = math.ceil(val/3)
            heapq.heappush(heap, -1*val)
            
        
        return ans