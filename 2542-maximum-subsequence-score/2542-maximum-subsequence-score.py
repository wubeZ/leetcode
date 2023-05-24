class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        arr = list(zip(nums1, nums2))
        
        arr.sort(key = lambda x: x[1], reverse = True)
        minHeap = []
        n1Sum = 0
        res = 0

        for n1, n2 in arr:
            n1Sum += n1
            heapq.heappush(minHeap,n1)

            if len(minHeap) > k:
                n1Pop = heapq.heappop(minHeap)
                n1Sum -= n1Pop
            
            if len(minHeap) == k:
                res = max(res, n1Sum * n2)
                
        return res