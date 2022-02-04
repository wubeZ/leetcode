class Solution:
    def hIndex(self, citations: List[int]) -> int:
        hindex = 0
        citations.sort(reverse = True)
        
        for index in range(len(citations)):
            if citations[index] >= index + 1:
                hindex += 1
                
        return hindex                        
            