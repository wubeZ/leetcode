class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        i = 0
        while i < len(heights)-1:
            diff = heights[i+1] - heights[i]
            
            if diff > 0:
                heapq.heappush(heap, diff)
                if ladders > 0:
                    ladders -=1
                else:
                    bricks -= heapq.heappop(heap)
                    
                if bricks < 0:
                    return i
            i += 1
        
        return len(heights)-1
                
                