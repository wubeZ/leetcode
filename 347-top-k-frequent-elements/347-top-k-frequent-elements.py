class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        arr = Counter(nums)
        kval = []
        ans = []
        for key in arr:
            kval.append((arr[key] , key))
            
        heapq._heapify_max(kval)
    
        for i in range(k):
            ans.append(heapq._heappop_max(kval)[1])
            
        return ans