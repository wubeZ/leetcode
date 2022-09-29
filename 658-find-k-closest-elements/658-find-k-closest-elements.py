class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = []
        ans = []
        
        for num in arr:
            heapq.heappush(heap, ((abs(num - x)), num))
        
        for i in range(k):
            ans.append(heapq.heappop(heap)[1])
        
        return sorted(ans)