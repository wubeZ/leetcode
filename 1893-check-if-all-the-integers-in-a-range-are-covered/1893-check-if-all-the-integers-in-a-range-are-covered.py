class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        maxVal = 0
        for i in range(len(ranges)):
            maxVal = max(maxVal, ranges[i][1])
        if maxVal < right:
            return False

        numberline = [0] *(maxVal + 2)
        for i in range(len(ranges)):
            numberline[ranges[i][0]] += 1
            numberline[ranges[i][1]+1] -= 1
        
        prefixSum = [0] * (maxVal + 1)
        
        for i in range(1,len(prefixSum)):
            prefixSum[i] = prefixSum[i-1] + numberline[i]
        
        for i in range(left, right+1):
            if prefixSum[i] == 0:
                return False
        
        return True