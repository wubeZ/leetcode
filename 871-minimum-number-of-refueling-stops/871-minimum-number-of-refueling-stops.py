class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        dp = [startFuel] * (len(stations)+1)
        for i in range(len(stations)): 
            for j in range(i+1, 0, -1): 
                if dp[j-1] >= stations[i][0]:
                    dp[j] = max(dp[j], dp[j-1] + stations[i][1])
        
        for i in range(len(dp)): 
            if dp[i]>=target: 
                return i
        return -1   