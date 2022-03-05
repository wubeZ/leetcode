class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        arr = Counter(words)
        kval = []
        ans = []
        
        for key in arr:
            kval.append((-arr[key] , key))
        
        heapq.heapify(kval)
        
        for i in range(k):
            ans.append(heapq.heappop(kval)[1])
    
        return ans

        