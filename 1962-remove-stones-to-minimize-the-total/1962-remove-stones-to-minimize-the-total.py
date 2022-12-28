class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = [-p for p in piles]
        heapq.heapify(heap)
        
        while k > 0:
            val = - heapq.heappop(heap)
            temp = math.ceil(val / 2)
            heapq.heappush(heap, -temp)
            k -= 1
        
        ans = 0
        for num in heap:
            ans += abs(num)
            
        return ans
        
        
            