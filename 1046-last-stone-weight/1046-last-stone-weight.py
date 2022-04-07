class Solution(object):
    def lastStoneWeight(self, stones):
        heap = [-x for x in stones]
        heapq.heapify(heap)
        
        if len(heap) == 1:
            return -heap[0]
        
        while len(heap) > 1:
            y = heapq.heappop(heap)
            x = heapq.heappop(heap)
            
            if x != y:
                z = abs(y) - abs(x)
                heapq.heappush(heap, -z)
        
        if not heap:
            return 0
        else:
            return -heap[0]