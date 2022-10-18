class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        maxValue = float("-inf")
        for i in range(len(trips)):
            maxValue = max(maxValue, trips[i][2])
        
        timeline = [0]*(maxValue+1)
        for i in range(len(trips)):
            timeline[trips[i][1]] += trips[i][0]
            timeline[trips[i][2]] -= trips[i][0]
        
        prefixsum = [0]*(len(timeline))
        
        for i in range(maxValue):
            prefixsum[i] = prefixsum[i - 1] + timeline[i]
        
        print(prefixsum)
        return max(prefixsum) <= capacity
        
        
            