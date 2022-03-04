class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        heapq.heapify(stones)
        
        if len(stones) == 1:
            return -stones[0]
            
        while len(stones) > 1 :
            y = heapq.heappop(stones)
            heapq.heapify(stones)
            x = heapq.heappop(stones)
            heapq.heapify(stones)
            
            if x != y:
                z = abs(y) - abs(x)
                heapq.heappush(stones, -z)
                heapq.heapify(stones)
        
        if not stones:
            return 0
        else:
            return -stones[0]
        
                
            