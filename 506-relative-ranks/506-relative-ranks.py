class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        heap = []
        d = { 1:"Gold Medal",
              2:"Silver Medal",
              3:"Bronze Medal" }
        
        for i in range(len(score)):
            heapq.heappush(heap,(-score[i],i))
            
        j = 1
        while heap:
            val = heapq.heappop(heap)
            index = val[1]
            if j in d:
                score[index] = d[j]
            else:
                score[index] = str(j)
            j += 1
        
        return score
        
        