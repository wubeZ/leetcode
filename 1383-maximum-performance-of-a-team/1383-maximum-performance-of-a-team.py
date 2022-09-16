class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        
        heap = []
        res = sSum = 0
        
        for e, s in sorted(zip(efficiency, speed), reverse=1):
            heapq.heappush(heap, s)
            
            sSum += s
            
            if len(heap) > k:
                sSum -= heapq.heappop(heap)
                
            res = max(res, sSum * e)
            
        return res % (10**9 + 7)