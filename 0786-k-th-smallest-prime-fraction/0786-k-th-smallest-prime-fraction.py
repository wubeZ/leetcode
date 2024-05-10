class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        
        heap = []
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                heapq.heappush(heap, (-1* (arr[i] / arr[j]), i, j))
                if len(heap) > k:
                    heapq.heappop(heap)
        
        i = heap[0][1]
        j = heap[0][2]
        
        return [arr[i], arr[j]]
            
        
        