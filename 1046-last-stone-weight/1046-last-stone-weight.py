class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq._heapify_max(stones)
        
        if len(stones) == 1:
            return stones[0]
            
        while len(stones) > 1 :
            y = heapq._heappop_max(stones)
            heapq._heapify_max(stones)
            x = heapq._heappop_max(stones)
            heapq._heapify_max(stones)
            if x != y:
                y -= x
                heapq.heappush(stones, y)
                heapq._heapify_max(stones)

        if not stones:
            return 0
        else:
            return stones[0]
        
                
            