class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        count = [0] * 1002
        for num in arr:
            count[num-1] = 1
        
        c = 0
        for i in range(1002):
            if c == k:
                return i
            
            if count[i] == 0:
                c += 1
        
        return i + (k - c + 1)