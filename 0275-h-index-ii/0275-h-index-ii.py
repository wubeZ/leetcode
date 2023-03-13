class Solution:
    def hIndex(self, citations: List[int]) -> int:
        left = -1
        right = len(citations)
        length = len(citations)
        
        while left + 1 < right:
            mid = left + (right - left)//2
            
            if citations[mid] < length - mid:
                left = mid
            else:
                right =  mid
        
        return length - right