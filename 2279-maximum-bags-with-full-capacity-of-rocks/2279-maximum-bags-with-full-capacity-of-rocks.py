class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        arr = list(zip(capacity, rocks))
        
        arr.sort(key = lambda x: x[0] - x[1])
        
        ans = 0
        for i in range(len(arr)):
            if additionalRocks - (arr[i][0] - arr[i][1]) < 0:
                break
            ans += 1
            additionalRocks -= (arr[i][0] - arr[i][1])
            
        return ans