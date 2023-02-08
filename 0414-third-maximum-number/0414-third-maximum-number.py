class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        heap = []
        seen = set()
        
        for num in nums:
            if num not in seen:
                heapq.heappush(heap, num)
                seen.add(num)
            
            if len(heap) > 3:
                heapq.heappop(heap)
        
        if len(heap) == 3:
            return min(heap)
        
        return max(nums)
        
        